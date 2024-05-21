# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"G544.00","system":"readv2"},{"code":"Gyu5D00","system":"readv2"},{"code":"19699.0","system":"readv2"},{"code":"61250.0","system":"readv2"},{"code":"57338.0","system":"readv2"},{"code":"18475.0","system":"readv2"},{"code":"31759.0","system":"readv2"},{"code":"29158.0","system":"readv2"},{"code":"31727.0","system":"readv2"},{"code":"33262.0","system":"readv2"},{"code":"10078.0","system":"readv2"},{"code":"40582.0","system":"readv2"},{"code":"100910.0","system":"readv2"},{"code":"49355.0","system":"readv2"},{"code":"8274.0","system":"readv2"},{"code":"94872.0","system":"readv2"},{"code":"11878.0","system":"readv2"},{"code":"70698.0","system":"readv2"},{"code":"17596.0","system":"readv2"},{"code":"33907.0","system":"readv2"},{"code":"40239.0","system":"readv2"},{"code":"I08","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('multiple-valve-dz-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["valve---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["valve---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["valve---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
