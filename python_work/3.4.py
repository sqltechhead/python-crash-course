def invite_guests (guest_list):
    for guest in guest_list:
        print(f"{guest.title()}, Please come to my dinner party.")

guest_list = ['yoda', 'chewbacca', 'han solo', 'luke skywalker', 'darth vader']

invite_guests(guest_list=guest_list)

print(f"{guest_list.pop(0)}, can't make it anymore. Oh no.")

invite_guests(guest_list=guest_list)

new_guest = 'leia skywalker'
guest_list.append(new_guest)

print(f"{new_guest.title()}, now wants to come.")

invite_guests(guest_list=guest_list)