results= {i:0 for i in range(1,5)}

## program check
try:
    import p1
    assert p1.f(17,15,19) == 4
    assert p1.f(29,14,19) == 15
    results[1] = 1
except:
    pass

## program check
try:
    import p2
    assert p2.f("blue water") == "bw"
    assert p2.f("to be or not to be") == "tbontb"
    assert p2.f("Cracow Poland") == "CP"
    results[2] = 1
except:
    pass

## program check
try:
    import p3
    assert p3.f("ax15") == False
    assert p3.f("mysmartphone") == False
    assert p3.f("water5") == True
    assert p3.f("1234567") == True
    results[3] = 1
except:
    pass

## program check
try:
    import p4
    assert p4.f("2+3") == 5
    assert p4.f("3-8+1") == -4
    assert p4.f("1+2-1+3+4") == 9
    results[4] = 1
except:
    pass

# Final results
print("\nTOTAL PTS:", sum(results.values()), results)
print()
#input("Press ENTER...")
