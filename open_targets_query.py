"""
Main entry point for the Open Targets Query script.
Returns a JSON response from given OPen Targets endpoint, and produces summary stats
"""
from pprint import pprint
import argparse
from lib.association_store import AssociationStore
from opentargets import OpenTargetsClient

class OpenTargetsQuery(object):
    '''Open Targets Query'''
    def __init__(self):
        args = []
        parser = argparse.ArgumentParser(description='OpenTargets client')
        parser.add_argument('-t', '--target', dest='target',
   	                        help='Run analysis for a target, for example -t ENSG00000197386')
        parser.add_argument('-d', '--disease', dest='disease',
   	                        help='Run analysis for a disease, for example -d Orphan_399')
        parser.add_argument('--test')

        args = parser.parse_args()
        self.request(args.target, "target")

    def request(self, arg, query_type):
        """
        Requests response from given endpoint
        Args:
            arg (str): Given command line argument to query endpoint with
            query_type (str): Parameter for RESTful api query
            url (str): Given RESTful api endpoint
        Returns:
            response: A JSON response
        """
        ot = OpenTargetsClient()
        a_for_target = ot.get_associations_for_target(arg)
        for a in a_for_target:
            print(a)
        #reply = requests.get(url,
        #                     params={query_type:arg})
        #pprint(reply.json())
        #AssociationStore(reply)
        #len(r['data'])

if __name__ == '__main__':
    OpenTargetsQuery()
