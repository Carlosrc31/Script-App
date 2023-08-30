
import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main(sample, batch):
    #Get the data of the two files
    data_sample = read_csv_to_dict(sample)
    data_batch = read_csv_to_dict(batch)
    
    #Iterate on every row in data batch
    for row_batch in data_batch:
        #New boolean variable to know if the item already exists 
        item_exists = False
        
        #Iterate on every row in data sample
        for row_sample in data_sample:
            #If the item is the same we sum the quantity
            if row_batch['Name'] == row_sample['Name']:
                item_exists = True
                row_sample['Quantity'] = (int(row_batch['Quantity']) + int(row_sample['Quantity']))
        
        #If the boolean doesn't change it means that the item doesn't exist and it'will be added. 
        if item_exists == False:
            #print("Se agregó " + str(row_batch))
            data_sample.append(row_batch)
    
    #print(data_sample)
    
    #It'll write the new file with changes
    write_list_of_dicts_to_csv("File_Edited.csv", data_sample)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv', 'grocery_batch_1.csv')
