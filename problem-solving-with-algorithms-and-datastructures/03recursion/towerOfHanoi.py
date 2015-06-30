__author__ = 'cloudera'


def move_tower(height, from_tower, to_tower, with_tower):
    if height >= 1:
        move_tower(height-1, from_tower, with_tower, to_tower)
        move_disk(from_tower, to_tower)
        move_tower(height-1, with_tower, to_tower, from_tower)


def move_disk(from_tower, to_tower):
    print 'moving disk from '+from_tower+' to '+to_tower


#main
move_tower(4, 'a', 'c', 'b')
