def calc_emisii_co2():
    print("🔧 Introduceți parametrii personalizați pentru estimare CO₂\n")

    populatie = int(input("Populația zonei (ex. 212752): "))
    procent_soferi = float(input("Procent posesori auto (ex. 50 pentru 50%): ")) / 100
    km_zi = float(input("Distanță medie zilnică per șofer (km): "))
    consum = float(input("Consum mediu (litri / 100km): "))
    emisii_litru = float(
        input("Emisii CO₂ per litru combustibil (kg/litru, ex. 2.68 pentru diesel): ")
    )
    calatorii_saptamanale = int(
        input("Nr de calatorii saptamanale ale unei persoane(masina) (ex. 3-4): ")
    )

    sapt_an = 52
    # Calcul general pt o zi - nr total de masini . 100 de masini / zi. 100g -> * 365 -> 190 zile. 90 masini, duminica is 10. 100 in fiecare timp de 4 zile.
    nr_masini = populatie * procent_soferi
    km_totali = nr_masini * km_zi
    litri_totali = (km_totali / 100) * consum
    emisii_totale = litri_totali * emisii_litru

    print(f"\n📊 Estimări generale:")
    print(f"• Număr mașini active zilnic: {int(nr_masini)}")
    print(f"• Km parcurși total zilnic: {km_totali:,.0f} km")
    print(
        f"• CO₂ emis zilnic: {emisii_totale:,.2f} kg ≈ {emisii_totale / 1000:.2f} tone"
    )
    print(
        f"• CO₂ emis anual: {emisii_totale * calatorii_saptamanale * sapt_an / 1000:,.2f} tone"  # 52 sapt pe an
    )
    # 3 calatorii * (365/7)

    print("\n🚗 Estimare reducere prin carpooling:")
    reducere_procent = (
        float(input("Procent șoferi care folosesc carpooling (ex. 10 pentru 10%): "))
        / 100
    )
    # pasageri = int(input("Număr pasageri/mașină (ex. 2): ")) # pt viitor

    masini_eliminate = nr_masini * reducere_procent  # 100 masini -1% -> 1 masina.
    print(f"• Masini eliminate astfel zilnic: {masini_eliminate:,.0f} masini")

    km_salvati = masini_eliminate * km_zi
    litri_salvati = (km_salvati / 100) * consum
    co2_salvat = litri_salvati * emisii_litru

    print(
        f"\n✅ CO₂ economisit zilnic: {co2_salvat:,.2f} kg ≈ {co2_salvat / 1000:.2f} tone"
    )

    CO2_econ_anual = (
        co2_salvat * calatorii_saptamanale * sapt_an / 1000
    )  # 52 sapt pe an

    print(f"🌍 CO₂ economisit anual: {CO2_econ_anual:,.2f} tone")

    litri_salvati_anual = litri_salvati * calatorii_saptamanale * sapt_an
    print(f"🌍 litri combustibil economisit anual: {litri_salvati_anual:,.2f} LITRI")

    print(
        f"🌍 Pret combustibil economisit anual: {litri_salvati_anual * 7.2:,.2f} RON, {litri_salvati_anual * 7.2 /5:,.2f} EUR"
    )
    # un copac salveaza -> 22kg pe an CO2 BCS - best case scenario
    # copac urban - 10 - 12kg

    co2_salvat_de_copac_anual = 20  # kg
    # 200kg de co2 an / 20 => copaci
    copaci = CO2_econ_anual * 1000 / co2_salvat_de_copac_anual
    print(f"🌍 Copaci necesari pentru a stinge CO2 economisit: {copaci:.0f} copaci")
    pret_estimativ_plantare_copac = 20  # ron
    print(
        f"🌍 Pret estimativ pentru plantarea acestor copaci necesari pentru a stinge CO2 economisit: {copaci * pret_estimativ_plantare_copac:,.2f} RON ,{copaci * pret_estimativ_plantare_copac / 5:,.2f} EUR "
    )

    ## 33k eur ca nu ai poluat.
    ## daca poluai - pierdeai 33k eur pe combustibil respectiv 12k eur pe copaci (care nu au randamanet in anul actual)
    # 45k eur pierdere anuala. care poate fi salvata.

    # costuri
    # - development aplicatie -> salar angajati, licente, sisteme.
    # - reclama
    # - intretinere - sv up, platesti google pt harta.
    # 2000 eur angajat -> 6 persoane - 3 back / 3 front - 3 luni > 18 salarii * 2k = 32k eur pt dev. - internshipper - 800 eur.

    # scopul proiectului este eco friendly - dar si costul economic are un impact:
    # 500k eur - ca sa salvezi 50k - > 500k au fost produsi vanzare petrol.


if __name__ == "__main__":
    calc_emisii_co2()
