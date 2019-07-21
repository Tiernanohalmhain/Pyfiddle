baselist = ['Mage', 'Knight', 'Paladin', 'Necromancer', 'Fighter', 'Barbarian', 'Bard', 'Brawler', 'Mechanist', 'King', 'Sage', 'Master', 'Rogue', 'Muse' , 'Wizard']
prefixlist = ['Demonic', 'Angelic', 'Golden', 'Lunar', 'Solar', 'Sidereal', 'Dark', 'Skeletal', 'Draconic', 'Enlightened', 'Immortal']
suffixlist1 = ['of', 'for', 'from']
suffixlist2 = ['Heaven', 'Arcadia', 'Hell', 'the Underworld', 'the Mountain', 'the Void', 'the Abyss', 'the City', 'the Eternal', 'the Broken', 'the Downtrodden', 'the People', 'the Beggar', 'the Fool', 'the Emperor', 'the Hierophant', 'the Bejeweled', 'the Beautiful', 'the Infinite', 'the Red', 'the Blue', 'the Black', 'the Green', 'the Elders', 'the Forgotten', 'the Forbidden', 'the Swamps', 'the Plains', 'the Isles', 'the Flames', 'the Crowns', 'the Blood', 'the White', 'the Bright', 'the Dark', 'the Dragon', 'the Wolf', 'the Lion', 'the Kind', 'the Wrathful', 'the Manifold', 'the Destroyer', 'the Creator']
import random
print(random.choice(prefixlist), random.choice(baselist), random.choice(suffixlist1) , random.choice(suffixlist2))
