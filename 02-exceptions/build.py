import argparse
import sys
sys.path.append('../..')

from pypperoni.cmake import CMakeFileGenerator

parser = argparse.ArgumentParser()
parser.add_argument('--nthreads', '-t', type=int, default=4,
                    help='Number of threads to use')
args = parser.parse_args()

c = CMakeFileGenerator('02-exceptions', outputdir='build', nthreads=args.nthreads)
c.add_file('main.py')
c.modules['main'].set_as_main()
c.run()
