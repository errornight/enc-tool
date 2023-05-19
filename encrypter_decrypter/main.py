from encrypter_decrypter import enc_tool as enc
import argparse
import json
from encrypter_decrypter.config import config
# Just styles
from colorama import Fore, Style, init
init(autoreset=True)




def main():
    parser = argparse.ArgumentParser(prog= config.NAME + config.VERSION, 
                                    description= config.DESCRIPTION)
    parser.add_argument('data', nargs='?', help="The message you want to encrypt.")
    parser.add_argument('-p', '--password', help="Password to encrypt or decrypt your data.", required=True)
    parser.add_argument('-d', '--decrypt', help="Add this for decryption", action="store_true")
    parser.add_argument('-s', '--save', help="Path to file that encrypted / decrypted data will be saved in.")
    parser.add_argument('-f', '--file', help="Path to file that you want encrypt / decrypt data in it.")
    args = parser.parse_args()

    if not args.decrypt:
        if args.file:
            data = enc.read_data(args.file)
            enc_data = enc.fernet_encrypt(data, args.password)

            path = enc.path_manager(args.file)
            file_path = args.save or f'{path[0]}encrypted_{path[1]}'
            enc.save_data(enc_data, file_path)
            print(Fore.BLUE + "Your data was encrypted succesfully.", 
              Style.BRIGHT + Fore.WHITE + f"Encrypted data saved in '{file_path}'",
              Style.DIM + f"Your password key: {args.password}",
              sep="\n")
        else:
            if not args.data:
                parser.error("Provide a data to encrypt!")

            enc_data = enc.fernet_encrypt(args.data, args.password)
            
            if args.save:
                enc.save_data(enc_data, args.save)
                print(Fore.BLUE + "Your data was encrypted succesfully.", 
                Style.BRIGHT + Fore.WHITE + f"Encrypted data saved in '{args.save}'",
                Style.DIM + f"Your password key: {args.password}",
                sep="\n")
            else:
                print(Fore.BLUE + "Your data was encrypted succesfully.", 
                    Style.BRIGHT + Fore.WHITE + enc_data,
                    Style.DIM + f"Your password key: {args.password}",
                    sep="\n")


    elif args.decrypt:
        if args.file:
            data = enc.read_data(args.file)
            dec_data = enc.fernet_decrypt(data, args.password)

            path = enc.path_manager(args.file)
            file_path = args.save or f'{path[0]}decrypted_{path[1]}'
            enc.save_data(dec_data, file_path)
            print(Fore.GREEN + "Your data was decrypted succesfully.", 
              Style.BRIGHT + Fore.WHITE + f"Decrypted data saved in '{file_path}'",
              sep="\n")
        
        else:
            if not args.data:
                parser.error("Provide a data to decrypt!")
            dec_data = enc.fernet_decrypt(args.data, args.password)

            if args.save:
                enc.save_data(dec_data, args.save)
                print(Fore.GREEN + "Your data was decrypted succesfully.", 
                    Style.BRIGHT + Fore.WHITE + f"Decrypted data saved in '{args.save}'",
                    sep="\n")
            else:
                print(Fore.GREEN + "Your data was decrypted succesfully.", 
                    Style.BRIGHT + Fore.WHITE + dec_data,
                    sep="\n")
                
    else:
        parser.error("Provide a message or file to encrypt or decrypt!")

if __name__ == '__main__':
    main()
    