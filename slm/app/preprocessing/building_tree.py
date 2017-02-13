

class BuildTree:
#This is a class for Building Trees
    def display_tree(self,cbcr,osact,form1,ni58,notice_tsx,notice_cbc,ni51,cbcact,ni54,form5,form6,tsx_manual):
        """
        :param cbcr: Canada Business Corporations Regulations dictionary
        :param osact: Ontario Securities Act dictionary
        :param form1: Form 58-101F1 Corporate Governance Disclosure dictionary
        :param ni58: National Instrument 58-101 Disclosure of Corporate Governance Practices dictionary
        :param notice_tsx: TSX Staff Notice 2015-0002 (September 10, 2015) - Subsections 461.1-461.4 and Section 464 Director Elections and Annual Meetings dictionary
        :param notice_cbc: Notice concerning notice-and-access regime recently adopted by the Canadian Securities Administrators dictionary
        :param ni51: National Instrument 51-102 Continuous Disclosure Obligations dictionary
        :param cbcact: Canada Business Corporations Act dictionary
        :param ni54: National Instrument 54-101 Communication with Beneficial Owners of Securities of a Reporting Issuer dictionary
        :param form5: Form 51-102F5 Information Circular dictionary
        :param form6: Form 51-102F6 Statement of Executive Compensation dictionary
        :param tsx_manual: TSX Company Manual dictionary
        :return: all the trees in list form
        """
        cbcr_tree = self.building_recursive_tree(cbcr)
        osact_tree = self.building_recursive_tree(osact)
        form1_tree = self.building_recursive_tree(form1)
        ni58_tree = self.building_recursive_tree(ni58)
        notice_tsx_tree = self.building_recursive_tree(notice_tsx)
        notice_cbc_tree = self.building_recursive_tree(notice_cbc)
        ni51_tree = self.building_recursive_tree(ni51)
        cbcact_tree = self.building_recursive_tree(cbcact)
        ni54_tree = self.building_recursive_tree(ni54)
        form5_tree = self.building_recursive_tree(form5)
        form6_tree = self.building_recursive_tree(form6)
        tsx_manual_tree = self.building_recursive_tree(tsx_manual)

        return cbcr_tree,osact_tree,form1_tree,ni58_tree,notice_tsx_tree,notice_cbc_tree,ni51_tree,cbcact_tree,\
               ni54_tree,form5_tree,form6_tree,tsx_manual_tree

    def building_recursive_tree(self,node):
        """
        This function builds a recursive tree
        :param node: input data in the form of manually built dictionary
        :return: a tree in the form of list
        """
        results = [node['id']]
        if len(node['children']) > 0:
            for child in node['children']:
                results.extend(self.building_recursive_tree(child))
        return results

