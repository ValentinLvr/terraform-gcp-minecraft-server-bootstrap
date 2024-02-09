#!/bin/bash
set -e
set -o pipefail

GCP_PROJECT=""
GCP_REGION=""
GCP_ZONE=""

# Function to display script usage
usage() {
 echo "Usage: [OPTIONS]"
 echo "Options:"
 echo " -h, --help      Display this help message"
 echo " -p, --project GCP_PROJECT   GCP project"
 echo " -r, --region GCP_REGION    GCP region"
 echo " -z, --region ZONE    GCP zone"
}

has_argument() {
    [[ ("$1" == *=* && -n ${1#*=}) || ( ! -z "$2" && "$2" != -*)  ]];
}

extract_argument() {
  echo "${2:-${1#*=}}"
}

handle_options() {
  while [ $# -gt 0 ]; do
    case $1 in
      -p | --project)
        if ! has_argument $@; then
          echo "Error: GCP project must be set"
          echo ""
          usage
          exit 1
        fi
        GCP_PROJECT=$(extract_argument $@)
        printf "GCP Project is set to $GCP_PROJECT \n"
        shift
        ;;
      -r | --region)
        if ! has_argument $@; then
          echo "Error: GCP region must be set"
          echo ""
          usage
          exit 1
        fi
        GCP_REGION=$(extract_argument $@)
        printf "GCP Region is set to $GCP_REGION \n"
        shift
        ;;
      -z | --zone)
        if ! has_argument $@; then
          echo "Error: GCP zone must be set"
          echo ""
          usage
          exit 1
        fi
        GCP_ZONE=$(extract_argument $@)
        printf "GCP Zone is set to $GCP_ZONE \n"
        shift
        ;;
      -h | --help)
        usage
        exit 0
        ;;
      *)
        echo "Unknown option: $1"
        echo ""
        usage
        exit 1
        ;;
    esac
    shift
  done
}

# Handle option flags
handle_options "$@"

if [[ $GCP_PROJECT == "" || $GCP_REGION == "" ]]; then
  printf "GCP project & region must be set via the --project and --region flags"
  echo ""
  usage
  exit 1
fi

if [[ $GCP_ZONE == "" ]]; then
  GCP_ZONE=$GCP_REGION-a
  printf "GCP zone was not specified. Setting it to $GCP_ZONE by default \n"
fi


printf "\n -> running initialization script with GCP_PROJECT=$GCP_PROJECT and GCP_REGION=$GCP_REGION ... \n"

# GCLOUD CONFIG
gcloud auth login
gcloud config set project $GCP_PROJECT

# REPLACE PROJECT, REGION & ZONE IN TERRAFORM & FUNCTION FILES
sed -i '' "s/GCP_PROJECT/$GCP_PROJECT/g" locals.tf start-server-function-python/main.py stop-server-function-python/main.py
sed -i '' "s/GCP_REGION/$GCP_REGION/g" locals.tf start-server-function-python/main.py stop-server-function-python/main.py
sed -i '' "s/GCP_ZONE/$GCP_ZONE/g" locals.tf start-server-function-python/main.py stop-server-function-python/main.py

# CREATE THE TERRAFORM STATE BUCKET
gcloud storage buckets create gs://terraform-minecraft-server 
printf "\n -> succesfully initialized \n"