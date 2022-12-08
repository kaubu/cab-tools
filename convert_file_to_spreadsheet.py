# {
#     "query": " lower hutt",
#     "totalResults": 120,
#     "results": {
#         "results": [
#             {
#                 "code": "KB00020510",
#                 "_score": 497.55545,
#                 "title": "<em>Hutt City</em> Libraries",
#                 "description": "<em>Hutt City</em> Libraries is made up of eight local libraries and two Clubhouses based in <em>Hutt City</em> which provide access to print and digital books, newspapers, magazines, DVDs, and CDs.   Many online resources are accessible for free for borrowers with a Library Card.\u00a0",
#                 "url": "https://www.cab.org.nz/community-directory/KB00020510",
#                 "sticky": false,
#                 "public": true,
#                 "tags": ["for hire", "family history", "local government", "cultural activities"],
#                 "type": "ServiceProvider",
#                 "region": "",
#                 "regions": ["Wellington"],
#                 "cities": ["Lower Hutt"],
#                 "content": "Hutt City Libraries is made up of eight local libraries and two Clubhouses based in Hutt City which provide access to print and digital books, newspapers, magazines, DVDs, and CDs.   Many online resources are accessible for free for borrowers with a Library Card.\u00a0 These include Generosity NZ for funding applications, Anestry.com and Findmypast for family history research, Road to IELTS for English language practice, Beamafilm for streaming movies and documentaries and Story Box Library for children.  Hutt City Libraries run events for all ages including storytime and book groups, author and science talks, fun events for tamariki and their wh\u0101nau, school holiday activities, computer classes, and JP clinics.  See website for more information or talk with their staff.  \u00a0",
#                 "htmlcontent": "<p><span style=\"color: #365f91;\">Hutt City Libraries is made up of eight local libraries and two Clubhouses based in Hutt City which provide access to print and digital books, newspapers, magazines, DVDs, and CDs. </span></p>\n<p><span style=\"color: #365f91;\">Many online resources are accessible for free for borrowers with a Library Card.&nbsp; These include Generosity NZ for funding applications, Anestry.com and Findmypast for family history research, Road to IELTS for English language practice, Beamafilm for streaming movies and documentaries and Story Box Library for children.</span></p>\n<p><span style=\"color: #365f91;\">Hutt City Libraries run events for all ages including storytime and book groups, author and science talks, fun events for tamariki and their wh\u0101nau, school holiday activities, computer classes, and JP clinics.</span></p>\n<p><span style=\"color: #365f91;\">See website for more information or talk with their staff.</span></p>\n<p>&nbsp;</p>",
#                 "openingHours": "War Memorial Library\nMon, Tue, Thu, Fri 9.30am - 6.30pm \nWed 9.30am - 8.30pm\nSat 9.30am - 5pm\nSun Closed\nFor other libraries check the website",
#                 "phoneNumber": "04 570 6633",
#                 "phoneNumberNote": null,
#                 "email": "libraries@huttcity.govt.nz",
#                 "emailNote": null,
#                 "website": "https://library.huttcity.govt.nz",
#                 "websiteNote": null,
#                 "physicalAddress": "Various",
#                 "serviceType": "Specialist tenant advocacy service",
#                 "location": null
#             },
#             {},
#             {},

import json
import csv

json_file = "cab_search.json"
csv_file = "cab_data.csv"

with open(json_file, "r") as f:
    data = json.load(f)

results = data["results"]["results"]

# for result in results:
#     # print(f"{:#}", result)
#     # input("\n\n Do you want to continue to next one? ")
#     for col in result.keys():
#         print(f"{col}    {result[col]}")
#         input("\n\n Do you want to continue to next one? ")

with open(csv_file, "w", encoding="utf-8", newline="`") as f:
    # Shamelessly stolen
    csv_writer = csv.writer(f)

    count = 0

    for result in results:
        if count == 0:
            header = result.keys()
            csv_writer.writerow(header)
            count += 1
        
        csv_writer.writerow(result.values())
