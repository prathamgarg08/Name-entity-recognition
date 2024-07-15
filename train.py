from ner.configuration.gcloud import Gcloud
obj=Gcloud()
obj.sync_folder_from_glcoud(gcp_bucket_url="nlp-ner",filename="archive.zip",destination="test")
