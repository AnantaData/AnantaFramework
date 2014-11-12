#!/usr/bin/env python

#
# Generated Fri Nov  7 07:49:05 2014 by generateDS.py version 2.13a.
#
# Command line options:
#   ('-o', '/home/lakmal/PycharmProjects/AnantaUi/ananta_profile/mining_profile_api.py')
#   ('-s', '/home/lakmal/PycharmProjects/AnantaUi/ananta_profile/mining_profile.py')
#   ('--super', 'mining_profile_api')
#
# Command line arguments:
#   /home/lakmal/PycharmProjects/AnantaUi/AnantaWorkspace/Ananta.xsd
#
# Command line:
#   /home/lakmal/Data Mining/generateDS-2.13a/generateDS.py -o "/home/lakmal/PycharmProjects/AnantaUi/ananta_profile/mining_profile_api.py" -s "/home/lakmal/PycharmProjects/AnantaUi/ananta_profile/mining_profile.py" --super="mining_profile_api" /home/lakmal/PycharmProjects/AnantaUi/AnantaWorkspace/Ananta.xsd
#
# Current working directory (os.getcwd()):
#   lakmal
#

import sys

import mining_profile_api as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class StepTypeSub(supermod.StepType):
    def __init__(self, No=None, Operation=None):
        super(StepTypeSub, self).__init__(No, Operation, )
supermod.StepType.subclass = StepTypeSub
# end class StepTypeSub


class ProfilesTypeSub(supermod.ProfilesType):
    def __init__(self, Profile=None):
        super(ProfilesTypeSub, self).__init__(Profile, )
supermod.ProfilesType.subclass = ProfilesTypeSub
# end class ProfilesTypeSub


class ProfileTypeSub(supermod.ProfileType):
    def __init__(self, No_attr=None, No=None, Name=None, Type=None, Steps=None):
        super(ProfileTypeSub, self).__init__(No_attr, No, Name, Type, Steps, )
supermod.ProfileType.subclass = ProfileTypeSub
# end class ProfileTypeSub


class MiningProfileTypeSub(supermod.MiningProfileType):
    def __init__(self, Name=None, TrainingData=None, TestData=None, Model=None):
        super(MiningProfileTypeSub, self).__init__(Name, TrainingData, TestData, Model, )
supermod.MiningProfileType.subclass = MiningProfileTypeSub
# end class MiningProfileTypeSub


class ModelTypeSub(supermod.ModelType):
    def __init__(self, Profiles=None):
        super(ModelTypeSub, self).__init__(Profiles, )
supermod.ModelType.subclass = ModelTypeSub
# end class ModelTypeSub


class StepsTypeSub(supermod.StepsType):
    def __init__(self, Step=None):
        super(StepsTypeSub, self).__init__(Step, )
supermod.StepsType.subclass = StepsTypeSub
# end class StepsTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MiningProfileType'
        rootClass = supermod.MiningProfileType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MiningProfileType'
        rootClass = supermod.MiningProfileType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MiningProfileType'
        rootClass = supermod.MiningProfileType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MiningProfileType'
        rootClass = supermod.MiningProfileType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from mining_profile_api import *\n\n')
        sys.stdout.write('import mining_profile_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
