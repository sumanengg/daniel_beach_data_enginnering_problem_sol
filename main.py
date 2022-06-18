import io
import sys
import zipfile

import requests
import os

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]
path = 'C:/Users/ACER/Downloads/depm/Exercises/Exercise-1/download'
isExists = os.path.exists(path)


def zip_download():
    try:
        if not isExists:
            os.mkdir(path)
            print("Download Directory has created")
        data1 = []
        file_cnt = 1
        for url in download_uris:
            response = requests.get(url=url)
            success = response.status_code
            filename = url.split('/')[-1]
            if success == 200:
                data = response.content
                file_path = "download/{}".format(filename)
                with io.open(file_path, "wb") as f:
                    f.write(data)
                    f.close()
                file_cnt += 1
            else:
                print("Error is there: " + str(success))
    except Exception as e:
        print("The error is " + str(e))
        sys.exit(1)


def zip_to_csv():
    try:
        for file in os.listdir(path):
            zip_file_path = path + '/' + file
            csv_file_path = path + '/'
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(csv_file_path)
                zip_ref.close()
                os.remove(zip_file_path)
    except Exception as e:
        print("The error is " + str(e))
        sys.exit(1)


def remove_zip():
    for file in os.listdir(path):
        if file.endswith('.zip'):
            os.remove(path + '/' + file)
    print("All ZIP deleted")


if __name__ == '__main__':
    try:
        zip_download()
        print("Download of all ZIP completed")
        zip_to_csv()
        print("Unzip completed succesfully")
        remove_zip()
        print("Job completed Successfully")
    except Exception as e:
        print("The job got failed due to " + str(e))
        sys.exit(1)
