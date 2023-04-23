channelNum = "25"

f = open(f"./text-data/{channelNum}-text-dump.txt")

content = f.readlines()

all_data = ""
for line in content:
    all_data += line

all_data = all_data.replace("\n", "")
all_data = all_data.replace("  ", " ")

sender1 = "Connor"
sender2 = "Erik"
sender3 = "Etienne"
#sender4 = "Marco"



chunked = all_data.split("*")

transcriptions = []
for line in chunked:
    print(line)
    print("\n")
    if f"{sender1}:" in line:
        line = line.replace(f"{sender1}:", "")
        transcriptions.append({
            "sender": f"{sender1} Shorten",
            "content": line,
            "channelNum": int(channelNum)
        })
    elif f"{sender2}:" in line:
        line = line.replace(f"{sender2}:", "")
        transcriptions.append({
            "sender": f"{sender2} Bernhardsson",
            "content": line,
            "channelNum": int(channelNum)
        })
    elif f"{sender3}:" in line:
        line = line.replace(f"{sender3}:", "")
        transcriptions.append({
            "sender": f"{sender3} Dilocker",
            "content": line,
            "channelNum": int(channelNum)
        })
    '''
    elif f"{sender4}:" in line:
        line = line.replace(f"{sender4}:", "")
        transcriptions.append({
            "sender": f"{sender4} Bianco",
            "content": line,
            "channelNum": int(channelNum)
        })
    '''


import json
json_object = json.dumps(transcriptions, indent=4)
with open(f"data/Weaviate-Podcast-{channelNum}.json", "w") as outfile:
    outfile.write(json_object)
