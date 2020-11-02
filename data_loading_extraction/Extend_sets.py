import os
import argparse
from tqdm import tqdm

"""Adds mouthings to pre-existing train, validation and test set"""

def get_args():
    parser = argparse.ArgumentParser(description='Parsing arguments like input path, output path, ...')
    parser.add_argument("--old_data", required=True, type=str, help="Path to existing train, dev and test set")
    parser.add_argument("--new_data", required=True, type=str, help="Path to new data set")
    parser.add_argument("--output_dir", default=os.getcwd(), type=str, help=("Path to output_dir"))

    return parser.parse_args()

def main(args):
    test_sign = []
    test_mouthings = []
    test_de = []

    dev_mouthings = []
    dev_de = []
    dev_sign = []

    full_set_mouthings = []
    full_set_sign = []
    full_set_de = []


    dev_de_old = []
    dev_sign_old = []

    test_de_old = []
    test_sign_old = []

    old_data = args.old_data
    new_data = args.new_data
    output_dir = args.output_dir

    #reading existing test and dev files for de and sign
    with open(os.fsdecode(os.path.join(old_data, "dev.de")),"r", encoding='utf8') as infile:
        dev_de_old = infile.readlines()
    
    with open(os.fsdecode(os.path.join(old_data, "dev.sign")), "r", encoding='utf8') as infile:
        dev_sign_old = infile.readlines()


    with open(os.fsdecode(os.path.join(old_data, "test.de")),"r", encoding='utf8') as infile:
        test_de_old = infile.readlines()
    
    with open(os.fsdecode(os.path.join(old_data, "test.sign")),"r", encoding='utf8') as infile:
        test_sign_old = infile.readlines()


    #reading full new data set with de, sign and mouthings

    with open(os.fsdecode(os.path.join(new_data, "Full_set.de")),"r", encoding='utf8') as infile:
        full_set_de = infile.readlines()
    
    with open(os.fsdecode(os.path.join(new_data, "Full_set.sign")),"r", encoding='utf8') as infile:
        full_set_sign = infile.readlines()

    with open(os.fsdecode(os.path.join(new_data, "Full_set.mouthings")),"r", encoding='utf8') as infile:
        full_set_mouthings = infile.readlines()

    print("Extending dev set:")
    for i in tqdm(range(len(dev_de_old))):
        for j in range(0,len(full_set_de)):


            if ((full_set_de[j] == dev_de_old[i]) and (full_set_sign[j] == dev_sign_old[i])):
                
                dev_sign.append(full_set_sign[j])
                dev_mouthings.append(full_set_mouthings[j])
                dev_de.append(full_set_de[j])


                del full_set_de[j]
                del full_set_sign[j]
                del full_set_mouthings[j]
                
                
                break
    
    print("Extending test set:")
    for i in tqdm(range(len(test_de_old))):
        for j in range(0,len(full_set_de)):


            if ((full_set_de[j] == test_de_old[i]) and (full_set_sign[j] == test_sign_old[i])):
                
                test_sign.append(full_set_sign[j])
                test_mouthings.append(full_set_mouthings[j])
                test_de.append(full_set_de[j])


                del full_set_de[j]
                del full_set_sign[j]
                del full_set_mouthings[j]
                
                
                break



        
    with open(os.fsdecode(os.path.join(output_dir + '/' + 'dev.mouthings')), 'a') as outfile:
                    outfile.write("".join(map(str, dev_mouthings)))

    with open(os.fsdecode(os.path.join(output_dir + '/' + 'dev.sign')), 'a') as outfile:
                    outfile.write("".join(map(str, dev_sign)))

    with open(os.fsdecode(os.path.join(output_dir + '/' + 'dev.de')), 'a') as outfile:
                    outfile.write("".join(map(str, dev_de)))




    with open(os.fsdecode(os.path.join(output_dir + '/' + 'test.mouthings')), 'a') as outfile:
                    outfile.write("".join(map(str, test_mouthings)))

    with open(os.fsdecode(os.path.join(output_dir + '/' + 'test.sign')), 'a') as outfile:
                    outfile.write("".join(map(str, test_sign)))

    with open(os.fsdecode(os.path.join(output_dir + '/' + 'test.de')), 'a') as outfile:
                    outfile.write("".join(map(str, test_de)))




    with open(os.fsdecode(os.path.join(output_dir + '/' + 'train.de')), 'a') as outfile:
                    outfile.write("".join(map(str, full_set_de)))

    with open(os.fsdecode(os.path.join(output_dir + '/' + 'train.sign')), 'a') as outfile:
                    outfile.write("".join(map(str, full_set_sign)))
    with open(os.fsdecode(os.path.join(output_dir + '/' + 'train.mouthings')), 'a') as outfile:
                    outfile.write("".join(map(str, full_set_mouthings)))


    print("New train sets: " + str(len(full_set_de)) + " " + str(len(full_set_sign)) + " " + str(len(full_set_mouthings)))
    print("New devset sign: " + str(len(dev_sign)))
    print("New devset mouthings : " + str(len(dev_mouthings)))
    print("New devset de: ", str(len(test_de)))
    print("New testset sign: " + str(len(test_sign)))
    print("New testset mouthings : " + str(len(test_mouthings)))
    print("New testset de: ", str(len(dev_de)))

if __name__=="__main__":
    args = get_args()
    main(args)