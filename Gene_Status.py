input = open('./FlyBase_Fields_download.txt', mode='rb')
output = open('./Melanogaster.txt', mode='wb')


for line in input:
    if "melanogaster" in line and "Current" in line:
        output.write(line)