"""Example using pyzillow."""
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults, GetUpdatedPropertyDetails
import argparse
# arguments
parser = argparse.ArgumentParser(description='zillow data example')
parser.add_argument('-a', '--address', help='address to search', default='1947 N Upland St, Arlington, VA, 22207', required=False)
parser.add_argument('-v', '--verbose', help='print more stuff', action='store_true')
parser.add_argument('-z', '--zipcode', help='zipcode', default=22207)
parser.add_argument('--apikey', help='zillow api key')
args = parser.parse_args()


# globals

address = args.address
zipcode = args.zipcode

# functions


def get_wrapper():
    """Set the API key properly."""
    zillow_data = ZillowWrapper(args.apikey)
    return zillow_data


def search_address(zillow_data):
    """Get results from address input and zipcode input."""
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    result = GetDeepSearchResults(deep_search_response)
    if args.verbose:
        print(result)
    return result


def get_details(zillow_id):
    """Get updated detailed property data."""
    zillow_data = get_wrapper()
    updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
    result = GetUpdatedPropertyDetails(updated_property_details_response)
    if args.verbose:
        print(result)
    return result


def main():
    """Run the API calls to show the example data."""
    zillow_data = get_wrapper()
    result = search_address(zillow_data)
    if args.verbose:
        print(result.zillow_id)
    all_details = get_details(result.zillow_id)
    if args.verbose:
        print(all_details.rooms)

if __name__ == "__main__":
    main()
    exit('success')
