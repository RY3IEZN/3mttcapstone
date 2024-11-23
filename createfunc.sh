# in your gcp terminal you can also run the g-cmd to create a function
# /bin/bash/

gcloud functions deploy save_user_input \
    --runtime python310 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point save_user_input

# make sure all the files are in the root of the directory
