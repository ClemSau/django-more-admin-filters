VERSION = (1, 3)
__version__ = ".".join(map(str, VERSION))


from .filters import (
    MultiSelectFilter, MultiSelectRelatedFilter, MultiSelectRelatedOnlyFilter,
    MultiSelectDropdownFilter, MultiSelectRelatedDropdownFilter, DropdownFilter,
    ChoicesDropdownFilter, RelatedDropdownFilter, BooleanAnnotationFilter
)
