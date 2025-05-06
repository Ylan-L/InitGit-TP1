from colorama import init, Fore, Style
4
init()
def display():
message= f"{Fore.GREEN}Ceci est une{Fore.CYAN}modification{Style.RESET_ALL}"
print(message)
if __name__ == "__main__":
display()