a = "ace, act, age, ago, aid, aim, air, ale, all, and, ant, any, ape, apt, arc, are, arm, art, ash, ask, asp, ass, ate, awe, bad, bag, bar, bat, bay, bed, bee, beg, bet, bid, big, bin, bit, boa, bog, boo, bow, box, boy, bra, bud, bug, bum, bun, bus, but, buy, cab, can, cap, car, cat, cod, cog, con, cop, cow, cry, cub, cup, cut, dab, dad, dam, day, den, dew, did, die, dig, dim, dip, dog, dot, dry, dub, dug, duo, dye, ear, eat, eel, egg, ego, elf, elk, ell, end, era, eve, ewe, eye, fad, fan, far, fat, fax, fee, few, fig, fin, fit, fix, flu, fly, fog, for, fox, fry, fun, fur".split(", ")
b = "able, arch, bald, band, bark, barn, base, bath, bead, beef, beep, belt, bend, best, bird, bite, blue, boat, bold, bone, book, boot, brag, brew, brim, bulb, bump, burn, bush, calm, cape, card, cart, cast, cave, chip, clap, claw, clip, coal, code, coil, cold, cone, cook, cool, cope, cord, core, cost, crew, crop, cute, dart, dawn, deep, deer, dime, dive, dock, dome, door, dose, drum, dune, echo, edge, edit, emit, envy, epic, even, exit, face, fade, fame, fare, fast, fate, fear, feed, file, fine, fire, fish, flag, flip, foam, foot, fork, frog, fuel, gate, gift, glow, glue, goat, gold, good, grab, grid, grin, grow, gulf, hand, hard, harm, harp, head, heat, herb, hero, hide, high".split(", ")
c = "apple, brace, brick, broad, brush, cable, charm, chase, clean, climb, cloud, clown, coach, color, crown, dance, debug, dodge, dozen, draft, drain, drive, eagle, eager, early, earth, elbow, event, fancy, fault, field, flake, flame, flash, flute, found, frame, frost, ghost, grape, grass, greed, guard, guest, happy, heart, hobby, horse, hotel, house, image, issue, jelly, joker, kneel, knife, label, laugh, lemon, magic, maple, medal, model, money, moral, motor, music, ocean, olive, orbit, outer, panel, piano, pilot, point, power, prize, quick, quiet, radio, range, rapid, reach, relax, reply, river, royal, score, sense, shade, shark, sheet, short, skill, snake, sound, spice, spoon, storm, table, tiger, title, toast, trade, trend, trust, union, value, wagon, watch".split(", ")
d = "abacus, baffle, bucket, camera, cancel, canyon, castle, circus, clover, couple, danger, decade, demand, desert, doctor, double, dragon, editor, effect, empire, escape, fabric, family, famous, fiddle, finger, forest, fossil, garage, garden, gentle, global, growth, hammer, health, heroic, hidden, impact, income, invest, island, jacket, jungle, kettle, ladder, liquid, listen, locket, magnet, market, mellow, minute, mirror, modern, muscle, narrow, nature, nickel, object, office, orange, outfit, palace, pastor, pepper, pocket, portal, prison, puzzle, quiver, racket, recent, reform, region, remote, rocket, saddle, sample, secret, shadow, silent, silver, single, spoken, static, stolen, symbol, tactic, talent, temple, timber, tunnel, unique, useful, vanish, victim, volume, wander, wealth, weapon, window, winner, wisdom, yellow, zephyr".split(", ")
e = "abandon, balance, blanket, captain, concern, conduct, cottage, crystal, declare, develop, diamond, display, discuss, drought, eclipse, educate, elastic, enhance, example, express, factory, fashion, feature, fitness, freedom, general, gravity, harvest, healthy, history, horizon, impress, inspire, jackpot, journal, justice, kitchen, lantern, library, logical, machine, manager, mystery, natural, nervous, observe, organic, passage, pattern, physics, popular, primary, process, promise, protect, quality, reality, recover, related, release, request, respect, scholar, science, serious, silence, similar, special, station, storage, strange, suggest, support, sustain, tension, texture, tourism, traffic, tragedy, tribute, unusual, victory, village, visitor, weather, welcome, western, whether, witness, wrapper, written, zealous, acquire, advance, amazing, battery, beneath, central, charter, comfort, correct, evening, feeling".split(", ")
f = "absolute, building, contract, dedicate, exercise, flexible, hospital, identify, industry, jealousy, kindness, learning, mobility, national, organize, paradise, positive, quantity, reaction, recovery, security, standard, suitable, tangible, vacation, weakness, wireless, zephyrus, activate, baseline, charming, consider, decrease, dominate, equation, guidance, headline, increase, latitude, manifest, nominate, opposite, priority, register, sensible, superior, valuable, withdraw, xenogamy, youthful, backpack, campaign, designer, economic, frontier, graduate, homeland, internet, language, mountain, notebook, outbreak, personal, question, regional, slippery, training, universe, vertical, wildlife, yourself, athletic, colorful, faithful, generous, historic, indicate, landmark, moderate, northern, overlook, position, specific, ultimate, velocity".split(", ")
g = "apartment, blueprint, challenge, dangerous, education, glamorous, highlight, important, knowledge, landscape, notorious, objective, potential, qualified, represent, signature, technical, variation, yesterday, confident, enjoyable, fortunate, grappling, household, identical, marketing, nutrition, offensive, principal, reference, transport, unlimited, workforce, xenophile, brilliant, developer, endurance, fantastic, goldsmith, hazardous, including, lifestyle, machinery, nocturnal, overthink, pragmatic, questions, transform, uncertain, visionary, whirlwind, youngster, zoologist, architect, broadcast, chocolate, direction, effective, forgotten, gratitude, introduce, judgement, lightning, newspaper, territory, underline, waterfall, wonderful, adventure".split(", ")
h = "adventurer, calculator, excitement, formidable, incredible, journalism, locomotive, noteworthy, operations, percentage, quarantine, skyscraper, technology, worthwhile, xenophobic, zoological, alphabetic, discussion, endangered, government, literature, revolution, transition, victorious, xenophobia, yellowwood, zoologists, atmosphere, bankruptcy, complexity, dedication, enthusiasm, graduation, hemisphere, industrial, jeopardize, leadership, navigation, outrageous, perfection, regulation, specialize, underneath, waterfront, tremendous, systematic, resolution, remarkable, persuasive, noticeable, motivation, historical, generation, foundation, definitive, consultant, appreciate, apprentice, beneficial, consistent, deliberate".split(", ")
acaount = 0
bcaount = 0
ccaount = 0
dcaount = 0
ecaount = 0
fcaount = 0
gcaount = 0
hcaount = 0
file1 = open("3letter.txt","w")
file2 = open("4letter.txt","w")
file3 = open("5letter.txt","w")
file4 = open("6letter.txt","w")
file5 = open("7letter.txt","w")
file6 = open("8letter.txt","w")
file7 = open("9letter.txt","w")
file8 = open("10letter.txt","w")

print("3 letters")
while len(a) > 0:
    temp = a[0]
    acaount += 1
    if len(a[0]) != 3:
        print(a[0])
    a.remove(a[0])
    if temp in a:
        print(temp)
    file1.write(f"{temp} \n")
print("")
print("")

print("4 letters")
while len(b) > 0:
    temp = b[0]
    bcaount += 1
    if len(b[0]) != 4:
        print(b[0])
    b.remove(b[0])
    if temp in b:
        print(temp)
    file2.write(f"{temp} \n")
print("")
print("")

print("5 letters")
while len(c) > 0:
    temp = c[0]
    ccaount += 1
    if len(c[0]) != 5:
        print(c[0])
    c.remove(c[0])
    if temp in c:
        print(temp)
    file3.write(f"{temp} \n")
print("")
print("")

print("6 letters")
while len(d) > 0:
    temp = d[0]
    dcaount += 1
    if len(d[0]) != 6:
        print(d[0])
    d.remove(d[0])
    if temp in d:
        print(temp)
    file4.write(f"{temp} \n")
print("")
print("")

print("7 letters")
while len(e) > 0:
    temp = e[0]
    ecaount += 1
    if len(e[0]) != 7:
        print(e[0])
    e.remove(e[0])
    if temp in e:
        print(temp)
    file5.write(f"{temp} \n")
print("")
print("")

print("8 letters")
while len(f) > 0:
    temp = f[0]
    fcaount += 1
    if len(f[0]) != 8:
        print(f[0])
    f.remove(f[0])
    if temp in f:
        print(temp)
    file6.write(f"{temp} \n")
print("")
print("")

print("9 letters")
while len(g) > 0:
    temp = g[0]
    gcaount += 1
    if len(g[0]) != 9:
        print(g[0])
    g.remove(g[0])
    if temp in g:
        print(temp)
    file7.write(f"{temp} \n")
print("")
print("")

print("10 letters")
while len(h) > 0:
    temp = h[0]
    hcaount += 1
    if len(h[0]) != 10:
        print(h[0])
    h.remove(h[0])
    if temp in h:
        print(temp)
    file8.write(f"{temp} \n")
print("")
print("")

print("number of words")
print(acaount, bcaount, ccaount, dcaount, ecaount, fcaount, gcaount, hcaount)

print("lsits")
print(a, b, c, d, e ,f ,g ,h)