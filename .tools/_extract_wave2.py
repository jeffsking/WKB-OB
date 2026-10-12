import json, os
os.chdir(r'E:\WKB-OB')
m = json.load(open('.tools/ebook_compile_manifest.json', encoding='utf-8'))
done_index_only = {
    "A review on superabsorbent polymers","Research_Advances_in_Superabsorbent_Polymers",
    "Superabsorbent_Polymers_and_Superabsorbe","Emerging_applications_of_stimuli_respons",
    "Stimuli_Responsive_Phase_Change_Material","edana_2022_absorbent-hygiene-products"
}
for e in m['books']:
    if e['name'] in ("Absorbent Technology (Chatterjee & Gupta)",
                     "Smart_Textiles_Wearables_拆解"):
        print("### CHAPTER:", e['name'], "| n=", e['n_chapters'], "| root:", e.get('root_file_rel'))
        for c in e['chapter_source_paths']:
            print("   CH:", c)
print("\n=== 剩余 P0 index_only（未做）===")
cnt=0
for e in m['books']:
    if e['priority']=='P0' and e['compile_as']=='index_only' and e['name'] not in done_index_only:
        cnt+=1
        print(f"   {e['name']}  ->  {e.get('root_file_rel')}")
print("   剩余 index_only 数:", cnt)
