class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #creating a new recursive function to enable us walk-through the group
    def walk_through(present_group):

        #base case
        #user is the end member  of a group. a user, in this case is not a group
        if user in present_group.get_users():
            return True
       
        # recursing through child group within the present groupi.e. subset group in bigger group(main group)
        for child_group in present_group.get_groups():
            return walk_through(child_group)#this returns the recursive function until the base function is achieved.

    # if the user is not a member of the group it would default to None, Hence, return walk_through(group) is True is used
    #and not just return walk_through(group)
    return walk_through(group) is True
   
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
child_user = "child_user"
sibling_user = "sibling_user"
parent_user = "parent_user"

#adding the users to particular groups
sub_child.add_user(sub_child_user)
child.add_user(child_user)
child.add_user(sibling_user)
parent.add_user(parent_user)

#adding the sub_child group to the child group
child.add_group(sub_child)
#adding the child group to the parent group
parent.add_group(child)

#trying out the edge cases
#for a known sub_child(sub_child_user) of a parent
print(is_user_in_group("sub_child_user", parent))

#for an unknown child(friend_of_user) of a parent
print(is_user_in_group("friend_of_user", parent))

#for an parent("parent_user") of a parent group
print(is_user_in_group("parent_user", parent))

#for an parent("child_user") of a parent group
print(is_user_in_group("child_user", parent))

#for an parent("sibling_user") of a parent group
print(is_user_in_group("sibling_user", parent)) 
