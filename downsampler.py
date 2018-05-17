"""Script to downsample R6:S data for final project."""

import re


sampler = re.compile("(201702)[0-1][0-9].+?PC.*")
subset = []
with open("datadump_S5.csv", encoding="windows-1252") as file:
    for line in file:
        if 'dateid' in line:
            subset.append(line.split(";"))
        if sampler.match(line):
            subset.append(line.split(";"))

with open("downsampled_datadump.csv", mode="w") as output_file:
    output_file.write("\n".join([",".join(line) for line in subset]))
