
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--login', type=str, required=True, help="Enter the player login.")
arg = parser.parse_args()

t_login = arg.login

print(t_login)