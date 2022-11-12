import speedtest

#check speed of downloading
download_speed = speedtest.Speedtest().download()
print(download_speed / (2**20))

#check speed of loading
upload_speed = speedtest.Speedtest().upload()
print(upload_speed / (2**20))

