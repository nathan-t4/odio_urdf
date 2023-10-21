import argparse
from urdfpy import URDF

def main(file="table.urdf"):
    robot = URDF.load(file)
    robot.show()    

if '__name__' == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--file", dest="file", type=str, default=None)

    args = arg_parser.parse_args()

    main(file=args.file)