from Country import *
from CountryCatalogue import *


def test_find_country(country_catalogue):
    print()
    print("Looking up country")
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cntry_obj = country_catalogue.find_country(cntry)
    if cntry_obj is None:
        print("-- Country not found in list")
    else:
        print(cntry_obj)


def test_set_population(country_catalogue):
    print()
    print("Setting population of country")
    item_found = False
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cPop = input("  --  Enter new population: ")
    cPop = cPop.strip()
    cPop = int(cPop.replace(",", ""))
    item_found = country_catalogue.set_population_of_country(cntry, cPop)
    if not item_found:
        print("  Country " + cntry + " is not in the current list")


def test_add_country(country_catalogue):
    print()
    cntry = input("-- Enter name of country to add: ")
    cntry = cntry.strip()
    thePop = input("      Enter the population: ")
    thePop = thePop.strip()
    cPop = int(thePop.replace(",", ""))
    theSz = input("      Enter the size(area): ")
    theSz = theSz.strip()
    cSz = float(theSz.replace(",", ""))
    theCont = input("      Enter the continent: ")
    theCont = theCont.strip()
    itemFound = country_catalogue.add_country(cntry, cPop, cSz, theCont)
    if not itemFound:
        print("  Country " + cntry + " is already in the current list")


def test_delete_country(country_catalogue):
    print()
    cntry = input("-- Enter name of country to delete: ")
    cntry = cntry.strip()
    country_catalogue.delete_country(cntry)


def test_filter_countries_continent(country_catalogue, theCont):
    lst = country_catalogue.filter_countries_by_continent(theCont)
    if len(lst) > 0:
        print()
        print("Countries in " + theCont + " are:")
        for cobj in lst:
            print(cobj)


def test_find_most_populous_continent(country_catalogue):
    rName, rPop = country_catalogue.find_most_populous_continent()
    print()
    print("The most populous continent is " + rName + " with a population of " + str(rPop))


def test_find_country_largest_pop(country_catalogue):
    rslt = country_catalogue.find_country_largest_pop()
    print()
    print("The country with the largest population is " + rslt.get_name())


def test_find_country_smallest_area(country_catalogue):
    rslt = country_catalogue.find_country_smallest_area()
    print()
    print("The country with the smallest area is " + rslt.get_name())


def test_filter_countries_by_pop_density(country_catalogue):
    print()
    lb = input("-- Enter the lower bound for population density: ")
    lb = float(lb.strip())
    ub = input("-- Enter the upper bound for population density: ")
    ub = float(ub.strip())
    rlst = country_catalogue.filter_countries_pop_density(lb, ub)
    if len(rlst) == 0:
        print("  No countries with density in that range found.")
    else:
        print("  Countries with density in this range are:")
        for ac in rlst:
            print(ac.get_name() + ", " + "density = " + str(ac.get_pop_density()))


def test_save_country_catalogue(cc, fname):
    print()
    print("Saving Country Catalogue")
    nitems = cc.save_country_catalogue(fname)
    print(" " + str(nitems) + " items written to file " + fname)


def main():
    cc = CountryCatalogue("continent.txt", "country.txt")
    # print initial catalogue
    cc.print_country_catalogue()
    # find a country
    # test_find_country(cc)
    # add a country, delete a country, print the new catalogue and find a country in the new catalogue
    # test_add_country(cc)
    # test_delete_country(cc)
    # print()
    # cc.print_country_catalogue()
    # test_find_country(cc)
    # set the area and population
    test_set_population(cc)
    # print various parts of the catalogue
    test_filter_countries_continent(cc, "Europe")
    # test the largest pop and smallest area
    test_find_country_largest_pop(cc)
    test_find_country_smallest_area(cc)
    # test filters
    test_filter_countries_by_pop_density(cc)
    test_find_most_populous_continent(cc)
    # print final catalogue and then output it to a file
    print()
    cc.print_country_catalogue()
    test_save_country_catalogue(cc, "output.txt")


main()
