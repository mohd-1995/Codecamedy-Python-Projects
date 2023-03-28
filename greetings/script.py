

# Write your code below:
from contextlib import contextmanager


@contextmanager
def generic(card_type, sender_name, recipient):
  card_file = open("card_file", "r")
  order = open("{} >_ generic.txt".format(sender_name), "w")
  try:
    order.write("Dear {}".format(recipient))
    order.write(card_file.read())
  finally:
    card_file.close()
    order.close()

with generic("thankyou_card.txt", "Mewnda", "Amanda") as order1:
  print("Card generated!!!!")


# Uncomment to run!
# with generic("thankyou_card.txt", "Mwenda", "Amanda") as order1:
#   print('Card Generated! \n')

# with open("Mwenda_generic.txt", "r") as first_order:
#   print(first_order.read())