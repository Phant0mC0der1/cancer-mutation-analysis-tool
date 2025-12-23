# Importing modules #
import pandas as pd
import matplotlib.pyplot as plt

def data_filtering_and_visualisation(file,site):
    # Loading and Filtering Data #
    tp53 = pd.read_csv(file, sep = "\t")
    tp53 = tp53[["Sample ID","Protein Change","Cancer Type","Cancer Type Detailed","Mutation Type"]] #trims down dataset to relevant columns

    # Identifying Mutation Hotspots and Types #
    tp53["Codon"] = tp53["Protein Change"].str.extract(r'(\d+)') #extracts codon
    hotspots = pd.DataFrame(tp53["Codon"].value_counts().head(10)) #gets top 10 most common codons
    hotspots.columns = ["Count"]
    mutation_types = tp53["Mutation Type"].value_counts()

    # Plotting the data #
    plt.figure(figsize=(10,6))
    plt.bar(hotspots.index, hotspots['Count'])
    plt.xlabel("Codon")
    plt.ylabel("Count")
    plt.title(f"Top 10 tp53 Mutation Hotspots by Codon in {site} cancer")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(8,8))
    plt.pie(
        mutation_types,
        labels=mutation_types.index,
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title(f"Mutation Types Distribution in {site} cancer", pad=20)  # Increased padding
    plt.axis('equal')
    plt.show()
    tp53.to_csv(f"C:/Users/dhash/Documents/Cross-Tissue Conservation of Tumor Supressor Mutation Hotspots/filtered_data/{site}_data_filtered.csv")

sites = []
while True: # Takes in relevant cancer sites through iteration
    site = input("Enter the cancer site:  ").lower()
    sites.append(site)
    while True:
        choice = input("Have you entered all your sites? \nType 'y' for yes and 'n' for no:  ").lower()
        if choice != "y" and choice != "n":
            print("Answer must be 'y' or 'n'")
        else:
            break
    if choice == "y":
        break

paths = []
while True: # Takes in complementary file paths through iteration
    path = input("Enter the coressponding file path:  ")
    paths.append(path)
    while True:
        choice = input("Have you entered all your paths? \nType 'y' for yes and 'n' for no:  ").lower()
        if choice not in ["y","n"]:
            print("Answer must be 'y' or 'n'")
        else:
            break
    if choice == "y":
        break

for i in range(0,len(sites)):
    data_filtering_and_visualisation(paths[i],sites[i]) # runs the analysis function for each cancer site using coressponding file path
