import argparse
import requests
from pprint import pprint

class OpenTargetsQuery():
	
   def request(arg):
      #https://www.targetvalidation.org/api/latest/public/search
      reply = requests.get('https://www.targetvalidation.org/api/latest/public/association/filter', params={"q":arg, "size":1})
      pprint(reply.json())


if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='OpenTargets client')
   parser.add_argument('-t', '--target', dest='target', help='Run analysis for a target, for example -t ENSG00000197386')
   parser.add_argument('-d', '--disease', dest='disease', help='Run analysis for a disease, for example -d Orphan_399')
   parser.add_argument('--test')
   
   args = parser.parse_args()
      
   query = OpenTargetsQuery
   query.request(args.target)
      