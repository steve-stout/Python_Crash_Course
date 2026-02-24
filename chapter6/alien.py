#Chapter 6 simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0['x_position'] = 0
alien_0['y_position'] =25
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just plugged an alien and got {new_points} points!")

del alien_0['points']
print(alien_0)

#No Points page 98
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

#when key value isnt set
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

