"""
Storage layer for ProjMAN
S3-compatible storage using MinIO
"""

import os
from pathlib import Path
from typing import Optional
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

class StorageService:
    """S3-compatible storage service using MinIO"""
    
    def __init__(self):
        self.endpoint = os.getenv("S3_ENDPOINT", "http://localhost:9000")
        self.access_key = os.getenv("S3_ACCESS_KEY", "minioadmin")
        self.secret_key = os.getenv("S3_SECRET_KEY", "minioadmin")
        self.bucket = os.getenv("S3_BUCKET", "agentize")
        
        # Initialize S3 client
        self.s3_client = boto3.client(
            's3',
            endpoint_url=self.endpoint,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
        
        # Ensure bucket exists
        self._ensure_bucket_exists()
    
    def _ensure_bucket_exists(self):
        """Create bucket if it doesn't exist"""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket)
            logger.info(f"Bucket '{self.bucket}' exists")
        except ClientError:
            try:
                self.s3_client.create_bucket(Bucket=self.bucket)
                logger.info(f"Bucket '{self.bucket}' created")
            except ClientError as e:
                logger.warning(f"Could not create bucket: {str(e)}")
    
    def upload_file(self, file_path: str, object_name: Optional[str] = None) -> str:
        """
        Upload a file to S3 storage
        
        Args:
            file_path: Path to file to upload
            object_name: S3 object name (defaults to file name)
        
        Returns:
            URL to uploaded file
        """
        if object_name is None:
            object_name = Path(file_path).name
        
        try:
            self.s3_client.upload_file(file_path, self.bucket, object_name)
            url = f"{self.endpoint}/{self.bucket}/{object_name}"
            logger.info(f"File uploaded successfully: {url}")
            return url
        except ClientError as e:
            raise Exception(f"File upload failed: {str(e)}")
    
    def upload_content(self, content: str, object_name: str, content_type: str = "text/plain") -> str:
        """
        Upload text content to S3 storage
        
        Args:
            content: Text content to upload
            object_name: S3 object name
            content_type: MIME type
        
        Returns:
            URL to uploaded content
        """
        try:
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=object_name,
                Body=content.encode('utf-8'),
                ContentType=content_type
            )
            url = f"{self.endpoint}/{self.bucket}/{object_name}"
            logger.info(f"Content uploaded successfully: {url}")
            return url
        except ClientError as e:
            raise Exception(f"Content upload failed: {str(e)}")
    
    def download_file(self, object_name: str, file_path: str):
        """
        Download a file from S3 storage
        
        Args:
            object_name: S3 object name
            file_path: Local path to save file
        """
        try:
            self.s3_client.download_file(self.bucket, object_name, file_path)
            logger.info(f"File downloaded successfully: {file_path}")
        except ClientError as e:
            raise Exception(f"File download failed: {str(e)}")
    
    def get_url(self, object_name: str) -> str:
        """Get URL for an object"""
        return f"{self.endpoint}/{self.bucket}/{object_name}"

