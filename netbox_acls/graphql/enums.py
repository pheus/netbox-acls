import strawberry

from ..choices import (
    ACLActionChoices,
    ACLAssignmentDirectionChoices,
    ACLFamilyChoices,
    ACLProtocolChoices,
    ACLRuleActionChoices,
    ACLRuleLogOptionChoices,
    ACLTypeChoices,
)

__all__ = (
    "ACLActionEnum",
    "ACLAssignmentDirectionEnum",
    "ACLFamilyEnum",
    "ACLProtocolEnum",
    "ACLRuleActionEnum",
    "ACLRuleLogOptionEnum",
    "ACLTypeEnum",
)

#
# Access List
#

ACLActionEnum = strawberry.enum(ACLActionChoices.as_enum())
ACLFamilyEnum = strawberry.enum(ACLFamilyChoices.as_enum())
ACLTypeEnum = strawberry.enum(ACLTypeChoices.as_enum())

#
# Access List Assignments
#

ACLAssignmentDirectionEnum = strawberry.enum(ACLAssignmentDirectionChoices.as_enum())

#
# Access List Rules
#

ACLProtocolEnum = strawberry.enum(ACLProtocolChoices.as_enum())
ACLRuleActionEnum = strawberry.enum(ACLRuleActionChoices.as_enum())
ACLRuleLogOptionEnum = strawberry.enum(ACLRuleLogOptionChoices.as_enum())
