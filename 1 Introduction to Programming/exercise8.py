##
# Compute total weight of two types of parts
#
WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

# Read number of parts from user
widget = int(input("Enter number of widgets: "))
gizmo = int(input("Enter number of gizmos: "))

#Compute the result
weight = widget * WIDGET_WEIGHT + gizmo * GIZMO_WEIGHT

# Display the result
print("Total weight is", weight, "grams.")
