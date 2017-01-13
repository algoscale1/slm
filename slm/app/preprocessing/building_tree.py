

class BuildTree:

    def display_tree(self,cbcr,osact,form1,ni58,notice_tsx,notice_cbc,ni51,cbcact,ni54,form5,form6,tsx_manual):
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
        results = [node['id']]
        if len(node['children']) > 0:
            for child in node['children']:
                results.extend(self.building_recursive_tree(child))
        return results

