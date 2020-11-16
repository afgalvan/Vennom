from sys import path
try:
    path.append("../public")
    from main import main
except:
    path.append("public")
    from main import main
main()
