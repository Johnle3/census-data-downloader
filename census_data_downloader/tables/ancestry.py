#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class AncestryDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "singleancestry"
    UNIVERSE = "people reporting single ancestry"
    RAW_TABLE_NAME = 'B04004'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "universe",
        '002E': "afghan",
        '003E': "albanian",
        '004E': "alsatian",
        '005E': "american",
        '006E': "arab",
        '007E': "egyptian",
        '008E': "iraqi",
        '009E': "jordanian",
        '010E': "lebanese",
        '011E': "moroccan",
        '012E': "palestinian",
        '013E': "syrian",
        '014E': "all_arab",
        '015E': "other_arab",
        '016E': "armenian",
        '017E': "assyrian_chaldean_syriac",
        '018E': "australian",
        '019E': "austrian",
        '020E': "basque",
        '021E': "belgian",
        '022E': "brazilian",
        '023E': "british",
        '024E': "bulgarian",
        '025E': "cajun",
        '026E': "canadian",
        '027E': "carpatho_rusyn",
        '028E': "celtic",
        '029E': "croatian",
        '030E': "cypriot",
        '031E': "czech",
        '032E': "czechoslovakian",
        '033E': "danish",
		'034E': "dutch",
        '035E': "eastern_european",
        '036E': "english",
        '037E': "estonian",
        '038E': "european",
        '039E': "finnish",
        '040E': "french_except_basque",
        '041E': "french_canadian",
        '042E': "german",
        '043E': "german_russian",
        '044E': "greek",
        '045E': "guyanese",
        '046E': "hungarian",
        '047E': "icelander",
        '048E': "iranian",
        '049E': "irish",
        '050E': "israeli",
        '051E': "italian",
        '052E': "latvian",
        '053E': "lithuanian",
        '054E': "luxemburger",
        '055E': "macedonian",
        '056E': "maltese",
        '057E': "new_zealander",
        '058E': "northern_european",
        '059E': "norwegian",
        '060E': "pennsylvania_german",
        '061E': "polish",
        '062E': "portuguese",
        '063E': "romanian",
        '064E': "russian",
        '065E': "scandinavian",
        '066E': "scotch-irish",
        '067E': "scottish",
        '068E': "serbian",
        '069E': "slavic",
        '070E': "slovak",
        '071E': "slovene",
        '072E': "soviet_union",
        '073E': "subsaharan_african",
        '074E': "cape_verdean",
        '075E': "ethiopian",
        '076E': "ghanaian",
        '077E': "kenyan",
        '078E': "liberian",
        '079E': "nigerian",
        '080E': "senegalese",
        '081E': "sierra_leonean",
        '082E': "somali",
        '083E': "south_african",
        '084E': "sudanese",
        '085E': "ugandan",
        '086E': "zimbabwean",
        '087E': "african",
        '088E': "other_subsaharan_african",
        '089E': "swedish",
        '090E': "swiss",
        '091E': "turkish",
        '092E': "ukranian",
        '093E': "welsh",
        '094E': "west_indian_except_hispanic_groups",
        '095E': "bahamian",
        '096E': "barbadian",
        '097E': "belizean",
        '098E': "bermudan",
        '099E': "british_west_indian",
        '100E': "dutch_west_indian",
        '101E': "haitian",
        '102E': "jamaican",
        '103E': "trinidadian_and_tobagonian",
        '104E': "us_virgin_islander",
        '105E': "west_indian",
        '106E': "other_west_indian",
        '107E': "yugoslavian",
        '108E': "other_groups"
    })
