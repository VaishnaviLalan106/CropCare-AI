"""
disease_info.py - Comprehensive Plant Disease Knowledge Base
Maps raw model classes (PlantVillage dataset) to human-readable names,
symptoms, causal agents, treatment regimens, and preventative practices.
"""

DISEASE_DATABASE = {
    "Apple___Apple_scab": {
        "display_name": "Apple - Apple Scab",
        "plant": "Apple",
        "condition": "Apple Scab",
        "status": "Diseased",
        "severity": "Moderate to High",
        "pathogen_type": "Fungal (Venturia inaequalis)",
        "symptoms": (
            "Dull olive-green to velvety brown-black circular lesions on leaves and fruit. "
            "Infected leaves may curl, turn yellow, and drop prematurely, weakening the tree."
        ),
        "favorable_conditions": "Cool (13-24°C), wet spring weather with prolonged leaf moisture.",
        "treatment": [
            "Apply fungicides such as myclobutanil, captan, or copper-based sprays early in spring.",
            "Rake and burn or compost fallen infected leaves to eliminate overwintering ascospore inoculum.",
            "Prune canopy during winter dormancy to promote rapid leaf drying through enhanced air circulation."
        ],
        "prevention": [
            "Plant scab-resistant cultivars (e.g., Liberty, Enterprise, Freedom).",
            "Maintain drip irrigation rather than overhead sprinklers.",
            "Apply urea spray to leaves just prior to autumn leaf drop to speed decomposition."
        ]
    },
    "Apple___Black_rot": {
        "display_name": "Apple - Black Rot (Frog-Eye Leaf Spot)",
        "plant": "Apple",
        "condition": "Black Rot",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Fungal (Diplodia seriata)",
        "symptoms": (
            "Small purple specks on leaves that enlarge into circular lesions with tan centers and purple margins ('frog-eye' appearance). "
            "Can cause limb cankers and rotting of mature fruit."
        ),
        "favorable_conditions": "Warm (24-27°C) temperatures combined with frequent rainfall or heavy dew.",
        "treatment": [
            "Prune out dead wood, fire blight mummies, and branch cankers at least 15 cm below infected tissue.",
            "Apply protective fungicides (e.g., thiophanate-methyl, captan) from tight cluster through harvest.",
            "Dispose of all infected mummified fruit left on trees or orchard floor."
        ],
        "prevention": [
            "Avoid mechanical damage to bark and branches during pruning or harvest.",
            "Ensure balanced fertilization; avoid excess nitrogen which creates susceptible lush growth.",
            "Inspect trees annually for early signs of trunk cankers."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "display_name": "Apple - Cedar Apple Rust",
        "plant": "Apple",
        "condition": "Cedar Apple Rust",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Gymnosporangium juniperi-virginianae)",
        "symptoms": (
            "Bright orange-yellow spots on upper leaf surfaces. Later, small tube-like fruiting structures (aecia) "
            "emerge on leaf undersides, releasing powdery spores."
        ),
        "favorable_conditions": "Requires proximity to Eastern Red Cedar / Juniper trees and damp spring conditions.",
        "treatment": [
            "Apply targeted fungicides (e.g., myclobutanil, mancozeb) starting at pink bud stage until petal fall.",
            "Prune and remove rust galls from nearby juniper and red cedar trees during winter months.",
            "Remove severely defoliated twigs to encourage secondary bud break."
        ],
        "prevention": [
            "Maintain a buffer zone: remove eastern red cedar trees within 1–2 miles of apple orchards where possible.",
            "Grow resistant apple varieties such as Redfree, Freedom, or Williams' Pride.",
            "Monitor nearby ornamental junipers for brown woody galls."
        ]
    },
    "Apple___healthy": {
        "display_name": "Apple - Healthy Foliage",
        "plant": "Apple",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Leaves exhibit uniform deep green coloration, firm texture, and no chlorosis, lesions, or curling.",
        "favorable_conditions": "Balanced soil fertility, adequate sunlight, and proper orchard management.",
        "treatment": [
            "No chemical intervention required.",
            "Maintain standard seasonal organic fertilizer or balanced NPK application.",
            "Continue routine scouting and preventive orchard sanitation."
        ],
        "prevention": [
            "Annual dormant pruning for sunlight penetration.",
            "Maintain consistent soil moisture and weed control around root zone.",
            "Apply protective horticultural oil during dormancy to suppress overwintering pests."
        ]
    },
    "Blueberry___healthy": {
        "display_name": "Blueberry - Healthy Foliage",
        "plant": "Blueberry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Leaves are smooth, glossy, medium to dark green with no spotting, necrosis, or edge burn.",
        "favorable_conditions": "Acidic soil (pH 4.5 - 5.5), well-drained organic matter, and consistent irrigation.",
        "treatment": [
            "No disease treatment required.",
            "Monitor soil pH periodically using sulfur amendments if pH drifts above 5.2.",
            "Mulch with pine bark or acid-forming pine needles to conserve moisture."
        ],
        "prevention": [
            "Use acid-loving organic fertilizers (e.g., ammonium sulfate or cottonseed meal).",
            "Avoid overhead irrigation; use drip lines at the bush base.",
            "Perform annual rejuvenation pruning on stems older than 6 years."
        ]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "display_name": "Cherry - Powdery Mildew",
        "plant": "Cherry",
        "condition": "Powdery Mildew",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Podosphaera clandestina)",
        "symptoms": (
            "White circular powdery fungal patches on young foliage and shoots. "
            "Infected leaves may curl upward, distort, and drop prematurely."
        ),
        "favorable_conditions": "Warm days (18-28°C), dry air, and shaded canopies with high relative humidity.",
        "treatment": [
            "Apply sulfur-based or potassium bicarbonate fungicides at first sign of infection.",
            "Spray systemic fungicides (e.g., triflumizole, quinoxyfen) during critical foliage expansion.",
            "Prune water sprouts and crowded inner branches to allow sunlight and airflow."
        ],
        "prevention": [
            "Avoid excessive late-season nitrogen applications that fuel susceptible tender flushes.",
            "Prune trees into an open center or central leader system for optimal aeration.",
            "Scout nursery stock before transplanting."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "display_name": "Cherry - Healthy Foliage",
        "plant": "Cherry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Foliage is vibrant green, structurally intact, and free from fungal dust, spots, or chewing damage.",
        "favorable_conditions": "Full sun, deep fertile soil, good drainage, and proper canopy pruning.",
        "treatment": [
            "No treatment needed.",
            "Maintain regular orchard watering during fruit swelling stages.",
            "Apply organic mulch around drip line."
        ],
        "prevention": [
            "Annual dormant copper spray to deter bacterial canker.",
            "Keep grass cut short around the base to deter moisture stagnation.",
            "Scout weekly during humid periods."
        ]
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "display_name": "Corn (Maize) - Gray Leaf Spot",
        "plant": "Corn (Maize)",
        "condition": "Gray Leaf Spot",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Fungal (Cercospora zeae-maydis)",
        "symptoms": (
            "Narrow, rectangular, tan-to-gray lesions restricted by leaf veins. "
            "Lesions coalesce over time, causing blighting of entire leaves and premature stalk senescence."
        ),
        "favorable_conditions": "Warm (24-30°C), humid weather (>90% RH) and continuous minimum-till maize fields.",
        "treatment": [
            "Apply foliar strobilurin or triazole fungicides (e.g., azoxystrobin, pyraclostrobin) at tassel emergence (VT-R1 stage).",
            "Chop and till crop debris post-harvest to speed biological breakdown of fungal residue.",
            "Harvest promptly to prevent stalk lodging."
        ],
        "prevention": [
            "Plant corn hybrids rated high in genetic resistance to Gray Leaf Spot.",
            "Rotate crops annually with non-host species (soybeans, alfalfa, or small grains).",
            "Avoid planting at excessively high plant densities in humid bottomland fields."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "display_name": "Corn (Maize) - Common Rust",
        "plant": "Corn (Maize)",
        "condition": "Common Rust",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Puccinia sorghi)",
        "symptoms": (
            "Golden-brown to cinnamon-brown powdery pustules (uredinia) scattered across both upper and lower leaf surfaces. "
            "Severe infection leads to chlorosis and leaf death."
        ),
        "favorable_conditions": "Moderate temperatures (16-25°C) with high humidity and frequent evening dews.",
        "treatment": [
            "Fungicides are justified if rust covers >5% of the leaf surface on upper canopy before whorl/tassel stage.",
            "Spray triazole or strobilurin fungicides labeled for sweet or field corn.",
            "Maintain soil potassium levels to improve plant cell wall resilience."
        ],
        "prevention": [
            "Select rust-resistant hybrids featuring the Rp gene family.",
            "Plant early in the season to escape late airborne spore showers transported from southern regions.",
            "Scout fields weekly starting in mid-vegetative stages."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "display_name": "Corn (Maize) - Northern Corn Leaf Blight",
        "plant": "Corn (Maize)",
        "condition": "Northern Leaf Blight",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Fungal (Exserohilum turcicum)",
        "symptoms": (
            "Large, elliptical, cigar-shaped grayish-green to tan lesions (2.5 to 15 cm long) on leaves. "
            "In damp conditions, dark olivaceous fungal spores form in the lesion centers."
        ),
        "favorable_conditions": "Moderate temperatures (18-27°C) with extended periods of rain and heavy morning dew.",
        "treatment": [
            "Apply fungicides (e.g., prothioconazole, trifloxystrobin) when lesions appear on the third leaf below the ear prior to silking.",
            "Shred and bury infected crop residue after harvest.",
            "Prioritize rescue spraying in seed production fields."
        ],
        "prevention": [
            "Plant resistant hybrids carrying Ht1, Ht2, or Ht3 resistance genes.",
            "Implement a two-year crop rotation out of corn.",
            "Balance nitrogen with adequate potassium fertilization."
        ]
    },
    "Corn_(maize)___healthy": {
        "display_name": "Corn (Maize) - Healthy Foliage",
        "plant": "Corn (Maize)",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Sturdy green stalks, wide arching leaves without lesions, stripes, or pustules.",
        "favorable_conditions": "Warm climate, fertile nitrogen-rich soil, and timely rainfall or irrigation.",
        "treatment": [
            "No chemical intervention needed.",
            "Maintain side-dress nitrogen schedule according to soil tests.",
            "Ensure regular irrigation during critical pollination/grain fill periods."
        ],
        "prevention": [
            "Regular scout monitoring for cutworms, armyworms, and early leaf spots.",
            "Follow certified seed treatment protocols for seedling vigor.",
            "Maintain proper plant spacing (approx. 30,000 plants/acre)."
        ]
    },
    "Grape___Black_rot": {
        "display_name": "Grape - Black Rot",
        "plant": "Grape",
        "condition": "Black Rot",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Fungal (Guignardia bidwellii)",
        "symptoms": (
            "Small, circular reddish-brown leaf spots with tiny black fruiting bodies (pycnidia) in a ring. "
            "Infected berries shrivel into hard, black, wrinkled mummies within days."
        ),
        "favorable_conditions": "Warm (21-32°C) weather with leaves remaining wet for 6 to 24 consecutive hours.",
        "treatment": [
            "Apply protective fungicides (e.g., mancozeb, captan) early in the season from 1-inch shoot growth to bloom.",
            "Prune out and destroy infected canes and remove all mummified fruit clusters during winter dormancy.",
            "Open the vineyard canopy by shoot thinning and leaf pulling around fruit clusters."
        ],
        "prevention": [
            "Train vines on trellis systems that maximize airflow and rapid drying.",
            "Plant resistant cultivars (e.g., Norton, Chancellor) if growing in high-disease-pressure zones.",
            "Keep vineyard floor free of wild grapevines that act as pathogen reservoirs."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "display_name": "Grape - Esca (Black Measles)",
        "plant": "Grape",
        "condition": "Esca (Black Measles)",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Fungal Complex (Phaeomoniella chlamydospora, Fomitiporia mediterranea)",
        "symptoms": (
            "'Tiger-stripe' chlorotic and necrotic patterns between leaf veins. "
            "Berries develop dark brown to purple speckles ('measles'), crack, and fail to mature."
        ),
        "favorable_conditions": "Vine stress, mature vineyards (>10 years), and major pruning wounds open to spores.",
        "treatment": [
            "No curative fungicide exists; management focuses on vineyard sanitation.",
            "Mark symptomatic vines in summer; prune them last in winter to avoid spreading fungal spores.",
            "Protect fresh pruning cuts with wound sealants, copper paste, or Trichoderma-based biofungicides."
        ],
        "prevention": [
            "Adopt double-pruning or delayed pruning techniques in late winter when spore flights are minimal.",
            "Sanitize pruning shears frequently between individual vines with 70% alcohol.",
            "Remove and incinerate dead vine trunks and wood."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "display_name": "Grape - Leaf Blight (Isariopsis Spot)",
        "plant": "Grape",
        "condition": "Leaf Blight",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Pseudocercospora cladosporioides / Phaeoisariopsis vitis)",
        "symptoms": (
            "Irregular, angular dark brown or reddish lesions on leaves, often bounded by small veins. "
            "Premature defoliation can occur late in the season, exposing clusters to sun scald."
        ),
        "favorable_conditions": "Warm, humid post-bloom conditions and dense, unmanaged vine canopies.",
        "treatment": [
            "Spray copper hydroxide, boscalid, or strobilurin fungicides labeled for grape foliar blights.",
            "Prune lower lateral leaves around grape clusters to enhance spray penetration and air movement.",
            "Clean fallen leaves from under the vine row."
        ],
        "prevention": [
            "Maintain canopy management through hedging and shoot positioning.",
            "Avoid excessive irrigation late in the season.",
            "Inspect vineyard rows for localized hotspots after rainy weeks."
        ]
    },
    "Grape___healthy": {
        "display_name": "Grape - Healthy Foliage",
        "plant": "Grape",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Lush, vibrant green lobed leaves with clean margins and sturdy tendrils supporting balanced shoot growth.",
        "favorable_conditions": "Sunny aspect, well-draining gravelly loam, and balanced canopy management.",
        "treatment": [
            "No disease treatment required.",
            "Continue standard trellis shoot positioning and weed suppression under the vine line.",
            "Maintain petiole testing for micronutrient balance (boron, magnesium, zinc)."
        ],
        "prevention": [
            "Routine dormant preventative sulfur/copper spray.",
            "Regular scouting for powdery mildew or leafhopper presence.",
            "Proper fruit load thinning to avoid vine exhaustion."
        ]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "display_name": "Orange - Citrus Greening (Huanglongbing)",
        "plant": "Orange / Citrus",
        "condition": "Huanglongbing (HLB)",
        "status": "Diseased",
        "severity": "Critical (Quarantine Disease)",
        "pathogen_type": "Bacterial (Candidatus Liberibacter asiaticus, vectored by Asian Citrus Psyllid)",
        "symptoms": (
            "Asymmetrical blotchy mottle chlorosis on leaves, yellow shoot flushes, and thickened corky veins. "
            "Fruit remains small, lopsided, poorly colored (green at stem end), with bitter inedible juice."
        ),
        "favorable_conditions": "Presence of the Asian Citrus Psyllid (Diaphorina citri) in warm subtropical regions.",
        "treatment": [
            "There is currently no cure for infected trees; infected commercial trees should be removed to protect the grove.",
            "Intensive vector control: apply targeted insecticides (e.g., imidacloprid, spirotetramat) to suppress psyllids.",
            "Apply foliar nutritional sprays (zinc, manganese, iron, potassium phosphite) to temporarily sustain tree vitality."
        ],
        "prevention": [
            "Plant only certified disease-free nursery trees sourced from enclosed insect-proof screenhouses.",
            "Regularly monitor psyllid populations using yellow sticky traps.",
            "Follow strict agricultural quarantine and transport regulations."
        ]
    },
    "Peach___Bacterial_spot": {
        "display_name": "Peach - Bacterial Spot",
        "plant": "Peach",
        "condition": "Bacterial Spot",
        "status": "Diseased",
        "severity": "Moderate to High",
        "pathogen_type": "Bacterial (Xanthomonas arboricola pv. pruni)",
        "symptoms": (
            "Small, water-soaked polygonal angular spots on leaves turning reddish-purple to dark brown. "
            "Centers often fall out, giving leaves a characteristic 'shot-hole' perforated appearance."
        ),
        "favorable_conditions": "Warm (21-29°C), humid weather with wind-driven rains and sandy soils.",
        "treatment": [
            "Apply copper bactericides during late dormant and early bud break stages.",
            "Apply oxytetracycline sprays at shuck split and cover sprays where permitted.",
            "Avoid high nitrogen applications that stimulate late soft vegetative growth."
        ],
        "prevention": [
            "Plant resistant peach varieties (e.g., Belle of Georgia, Clayton, Candor).",
            "Establish windbreaks in sandy soil regions to minimize wind-borne grit abrasion on leaves.",
            "Avoid overhead irrigation."
        ]
    },
    "Peach___healthy": {
        "display_name": "Peach - Healthy Foliage",
        "plant": "Peach",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Long, lanceolate, deep green leaves with crisp serrated edges and no perforations or spots.",
        "favorable_conditions": "Full sunlight, well-drained sandy loam soil, and open-center canopy architecture.",
        "treatment": [
            "No disease control needed.",
            "Maintain fruit thinning to ensure optimal peach fruit size and branch support.",
            "Water regularly during fruit pit-hardening and final swell."
        ],
        "prevention": [
            "Dormant copper/oil spray for leaf curl and scale prevention.",
            "Keep the trunk base clear of tall grass and weeds.",
            "Regular pruning to maintain vase/open-center structure."
        ]
    },
    "Pepper,_bell___Bacterial_spot": {
        "display_name": "Bell Pepper - Bacterial Spot",
        "plant": "Bell Pepper",
        "condition": "Bacterial Spot",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Bacterial (Xanthomonas campestris pv. vesicatoria)",
        "symptoms": (
            "Small, circular to irregular water-soaked spots on leaves that turn brown with yellow haloes. "
            "Infected leaves turn yellow and drop prematurely, causing sunscald on developing peppers."
        ),
        "favorable_conditions": "Warm (24-30°C) temperatures combined with high humidity, heavy rains, or sprinkler irrigation.",
        "treatment": [
            "Spray fixed copper bactericide mixed with mancozeb for improved bacterial efficacy.",
            "Remove and destroy severely infected pepper plants to curb field spread.",
            "Avoid working in pepper fields when foliage is wet from dew or rain."
        ],
        "prevention": [
            "Use certified disease-free and hot-water-treated pepper seeds.",
            "Plant pepper varieties with genetic resistance races (X1 through X5).",
            "Rotate solanaceous crops out of the field for a minimum of 2 years."
        ]
    },
    "Pepper,_bell___healthy": {
        "display_name": "Bell Pepper - Healthy Foliage",
        "plant": "Bell Pepper",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Broad, vibrant green leaves with smooth margins and sturdy stems bearing white flowers or healthy fruit.",
        "favorable_conditions": "Warm soil, consistent moisture, high organic matter, and full sunlight.",
        "treatment": [
            "No treatment needed.",
            "Side-dress with balanced calcium-potassium fertilizer to avoid blossom end rot.",
            "Maintain mulch around root zone."
        ],
        "prevention": [
            "Use drip irrigation under plastic mulch.",
            "Monitor weekly for aphids, thrips, and hornworms.",
            "Maintain optimal staking or cage support."
        ]
    },
    "Potato___Early_blight": {
        "display_name": "Potato - Early Blight",
        "plant": "Potato",
        "condition": "Early Blight",
        "status": "Diseased",
        "severity": "Moderate to High",
        "pathogen_type": "Fungal (Alternaria solani)",
        "symptoms": (
            "Dark brown to black lesions featuring characteristic concentric rings resembling a target board. "
            "Usually initiates on older lower foliage, spreading upward as plants mature and suffer tuber stress."
        ),
        "favorable_conditions": "Warm temperatures (24-29°C) alternating between wet and dry conditions.",
        "treatment": [
            "Apply protectant fungicides (chlorothalonil, mancozeb) starting at row closure.",
            "Rotate with strobilurin or SDHI fungicides (e.g., boscalid) for resistance management.",
            "Ensure adequate nitrogen and potassium fertility; stressed plants are significantly more susceptible."
        ],
        "prevention": [
            "Plant certified disease-free seed tubers.",
            "Employ a 3-year crop rotation avoiding potatoes, tomatoes, and eggplants.",
            "Eliminate volunteer potato plants and nightshade weeds near fields."
        ]
    },
    "Potato___Late_blight": {
        "display_name": "Potato - Late Blight",
        "plant": "Potato",
        "condition": "Late Blight (Irish Famine Pathogen)",
        "status": "Diseased",
        "severity": "Critical",
        "pathogen_type": "Oomycete / Water Mold (Phytophthora infestans)",
        "symptoms": (
            "Water-soaked, dark irregular lesions rapidly turning pale green to dark brown/black. "
            "A delicate white fuzzy mold appears on leaf undersides in humid conditions. Entire canopy collapses rapidly."
        ),
        "favorable_conditions": "Cool to moderate temperatures (15-22°C) with persistent humidity (>90%) and rain.",
        "treatment": [
            "Immediately apply systemic fungicides (e.g., cymoxanil, mandipropamid, fluopicolide).",
            "Destroy infected cull piles and heavily infested fields to prevent spore escape to surrounding regions.",
            "Desiccate or kill vines 2-3 weeks before harvest to prevent tuber contamination."
        ],
        "prevention": [
            "Scout fields religiously using regional late-blight forecast warning systems (e.g., Blitecast).",
            "Plant certified late-blight resistant potato cultivars.",
            "Never leave potato tubers in unburied cull piles over winter."
        ]
    },
    "Potato___healthy": {
        "display_name": "Potato - Healthy Foliage",
        "plant": "Potato",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Compound leaves are lush green, erect, showing vigorous vegetative spread across the hills.",
        "favorable_conditions": "Loose, well-aerated sandy loam soil, moderate temperatures, and uniform hilling.",
        "treatment": [
            "No chemical treatments required.",
            "Continue regular hilling to protect developing tubers from sunlight exposure.",
            "Maintain uniform drip moisture to prevent tuber growth cracks."
        ],
        "prevention": [
            "Maintain weekly scouting for Colorado potato beetle and potato leafhopper.",
            "Ensure proper soil test based fertilization.",
            "Monitor canopy closure for adequate ventilation."
        ]
    },
    "Raspberry___healthy": {
        "display_name": "Raspberry - Healthy Foliage",
        "plant": "Raspberry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Distinctive serrated, pinnately compound green leaves with pale silver undersides and vigorous primocanes.",
        "favorable_conditions": "Rich organic soil, mild climate, good root drainage, and trellis support.",
        "treatment": [
            "No disease treatment required.",
            "Thin out crowded primocanes to 4-6 canes per linear foot of row.",
            "Mulch with wood chips to conserve moisture and suppress weeds."
        ],
        "prevention": [
            "Prune out floricanes immediately after fruiting to improve airflow.",
            "Avoid planting in soil where tomatoes, potatoes, or peppers were grown in past 4 years (Verticillium risk).",
            "Use trickle irrigation to keep foliage completely dry."
        ]
    },
    "Soybean___healthy": {
        "display_name": "Soybean - Healthy Foliage",
        "plant": "Soybean",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Trifoliate leaves are emerald green, erect, uniformly spaced, with vigorous nodulation on roots.",
        "favorable_conditions": "Warm sunny days, adequate phosphorus and potassium, and effective Rhizobium nodulation.",
        "treatment": [
            "No treatment needed.",
            "Scout for early soybean cyst nematode symptoms or Japanese beetles.",
            "Ensure consistent moisture during pod development (R3-R5 stages)."
        ],
        "prevention": [
            "Rotate crops annually with non-legume crops (maize, wheat).",
            "Inoculate seed with Bradyrhizobium japonicum when planting in new ground.",
            "Use certified seed with Phytophthora root rot resistance genes."
        ]
    },
    "Squash___Powdery_mildew": {
        "display_name": "Squash - Powdery Mildew",
        "plant": "Squash / Cucurbit",
        "condition": "Powdery Mildew",
        "status": "Diseased",
        "severity": "Moderate to High",
        "pathogen_type": "Fungal (Podosphaera xanthii / Erysiphe cichoracearum)",
        "symptoms": (
            "White talcum-powder-like spots on both upper and lower leaf surfaces, petioles, and stems. "
            "Leaves turn yellow, dry out, become brittle, and die, exposing squash to sunscald."
        ),
        "favorable_conditions": "Warm (20-27°C), dry days with high relative humidity at night, shaded dense foliage.",
        "treatment": [
            "Apply biofungicides (Bacillus amyloliquefaciens), potassium bicarbonate, or neem oil at first sign.",
            "Apply systemic fungicides (e.g., myclobutanil, cyflufenamid) alternating modes of action.",
            "Remove and compost infected leaves if infection is confined to a few lower leaves."
        ],
        "prevention": [
            "Select powdery mildew resistant squash cultivars (PMR varieties).",
            "Provide ample spacing between hills (1.5-2 meters) to encourage vigorous airflow.",
            "Water early in the morning using soaker hoses."
        ]
    },
    "Strawberry___Leaf_scorch": {
        "display_name": "Strawberry - Leaf Scorch",
        "plant": "Strawberry",
        "condition": "Leaf Scorch",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Diplocarpon earlianum)",
        "symptoms": (
            "Numerous small, irregular purple-red or dark brown blotches covering leaves. "
            "Unlike leaf spot, lesions do not develop white centers. Leaves dry up, turn brown, and look scorched."
        ),
        "favorable_conditions": "Prolonged leaf wetness during warm, rainy periods in spring and early summer.",
        "treatment": [
            "Mow and remove old strawberry leaves immediately after harvest renovation.",
            "Apply protective fungicides (e.g., captan, pyraclostrobin) during spring foliage flush.",
            "Keep strawberry beds free of competing weeds."
        ],
        "prevention": [
            "Plant resistant strawberry cultivars (e.g., Allstar, Jewel, Earliglow).",
            "Plant in well-drained, raised beds using straw or plastic mulch.",
            "Avoid overhead sprinkler irrigation."
        ]
    },
    "Strawberry___healthy": {
        "display_name": "Strawberry - Healthy Foliage",
        "plant": "Strawberry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Low-growing trifoliate deep green leaves with crisp toothed margins, strong crowns, and clean runners.",
        "favorable_conditions": "Sunny aspect, rich sandy loam soil with good compost, and pine needle or straw mulching.",
        "treatment": [
            "No chemical treatment required.",
            "Perform post-harvest renovation (mowing and fertilizing) to promote fresh crown growth.",
            "Maintain clean straw mulching under ripening fruit."
        ],
        "prevention": [
            "Scout for two-spotted spider mites and tarnished plant bugs.",
            "Replace perennial strawberry beds every 3-4 years to avoid disease build-up.",
            "Maintain drip irrigation lines under mulch."
        ]
    },
    "Tomato___Bacterial_spot": {
        "display_name": "Tomato - Bacterial Spot",
        "plant": "Tomato",
        "condition": "Bacterial Spot",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Bacterial (Xanthomonas spp.)",
        "symptoms": (
            "Small, dark, greasy water-soaked spots (1-3 mm) on leaves that turn brown-black with yellow rings. "
            "Can cause significant defoliation, sunburn on fruit, and scab-like fruit lesions."
        ),
        "favorable_conditions": "Warm (24-30°C), wet conditions with driving wind-borne rains or sprinkler splashing.",
        "treatment": [
            "Spray copper bactericide combined with mancozeb to overcome copper tolerance.",
            "Apply systemic acquired resistance (SAR) inducers like acibenzolar-S-methyl where available.",
            "Prune infected lower branches during dry sunny weather."
        ],
        "prevention": [
            "Use certified pathogen-free seeds treated with hot water or hydrochloric acid.",
            "Avoid overhead irrigation; use soil-level drip lines.",
            "Rotate tomato fields with non-solanaceous crops for 2 to 3 years."
        ]
    },
    "Tomato___Early_blight": {
        "display_name": "Tomato - Early Blight",
        "plant": "Tomato",
        "condition": "Early Blight",
        "status": "Diseased",
        "severity": "Moderate to High",
        "pathogen_type": "Fungal (Alternaria solani)",
        "symptoms": (
            "Brown-to-black spots with distinct concentric rings ('target' appearance) starting on older lower foliage. "
            "Yellowing tissue surrounds the lesions, leading to extensive leaf loss and collar rot on stems."
        ),
        "favorable_conditions": "Warm temperatures (24-29°C) with alternating heavy dew, rain, and dry sunshine.",
        "treatment": [
            "Remove lower infected leaves to prevent spores splashing higher up the plant.",
            "Apply protectant fungicides (chlorothalonil, copper, or mancozeb) on a 7-10 day schedule.",
            "Mulch heavily around the plant base to create a physical barrier against soil-borne spores."
        ],
        "prevention": [
            "Stake or cage tomato plants to keep foliage elevated off the ground.",
            "Implement a 3-year crop rotation without tomatoes, potatoes, or eggplants.",
            "Water only at ground level early in the morning."
        ]
    },
    "Tomato___Late_blight": {
        "display_name": "Tomato - Late Blight",
        "plant": "Tomato",
        "condition": "Late Blight",
        "status": "Diseased",
        "severity": "Critical",
        "pathogen_type": "Oomycete / Water Mold (Phytophthora infestans)",
        "symptoms": (
            "Large, irregular, water-soaked grayish-green spots that expand rapidly into dark brown soggy patches. "
            "Delicate white fungal-like growth appears on leaf undersides in humid conditions. Stems turn dark and collapse."
        ),
        "favorable_conditions": "Cool, wet, cloudy weather (15-22°C) with high relative humidity (>90%).",
        "treatment": [
            "Act quickly: spray targeted late-blight fungicides (e.g., chlorothalonil, cymoxanil, mandipropamid).",
            "Remove and bag infected plants completely on dry days to avoid dispersing billions of airborne spores.",
            "Never compost late-blight infected plant material; dispose in sealed trash."
        ],
        "prevention": [
            "Choose late-blight resistant varieties (e.g., Defiant, Mountain Merit, Plum Regal).",
            "Space plants generously to promote rapid air drying.",
            "Monitor regional agricultural extension disease alerts."
        ]
    },
    "Tomato___Leaf_Mold": {
        "display_name": "Tomato - Leaf Mold",
        "plant": "Tomato",
        "condition": "Leaf Mold",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Passalora fulva / Cladosporium fulvum)",
        "symptoms": (
            "Pale yellow spots with indistinct margins on upper leaf surfaces. "
            "The undersides of these yellow patches develop an olive-green to grayish velvety fungal mold."
        ),
        "favorable_conditions": "High relative humidity (>85%) and warm temperatures (21-24°C); common in greenhouses and high tunnels.",
        "treatment": [
            "Dramatically improve greenhouse ventilation using exhaust fans and horizontal airflow fans.",
            "Prune lower suckers and dense foliage to allow light and dry air to penetrate the canopy.",
            "Spray fungicides such as chlorothalonil, copper hydroxide, or cyazofamid."
        ],
        "prevention": [
            "Plant tomato cultivars with Cf resistance genes.",
            "Maintain greenhouse relative humidity below 85% through heating and venting.",
            "Avoid wet leaf surfaces overnight."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "display_name": "Tomato - Septoria Leaf Spot",
        "plant": "Tomato",
        "condition": "Septoria Leaf Spot",
        "status": "Diseased",
        "severity": "Moderate to High",
        "pathogen_type": "Fungal (Septoria lycopersici)",
        "symptoms": (
            "Numerous small, circular spots (1.5-3 mm) with gray or tan centers and dark brown margins. "
            "Tiny black specks (pycnidia) are visible inside the centers. Severe defoliation progresses from base upward."
        ),
        "favorable_conditions": "Warm temperatures (20-25°C) and extended wet weather or frequent overhead sprinkling.",
        "treatment": [
            "Prune off affected lower leaves immediately at first onset.",
            "Apply copper-based fungicides, chlorothalonil, or mancozeb at 7-day intervals.",
            "Apply organic mulch (straw, paper, or plastic) to stop rain from splashing spores from soil onto leaves."
        ],
        "prevention": [
            "Keep plants staked, pruned, and well aerated.",
            "Clean up all tomato garden debris thoroughly at the end of the season.",
            "Practice a 3-year crop rotation."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "display_name": "Tomato - Two-Spotted Spider Mites",
        "plant": "Tomato",
        "condition": "Two-Spotted Spider Mites",
        "status": "Pest Infestation",
        "severity": "Moderate to High",
        "pathogen_type": "Arachnid Pest (Tetranychus urticae)",
        "symptoms": (
            "Fine yellow or white stippling (tiny dots) on upper leaf surfaces. "
            "Fine silky webbing appears on leaf undersides and stem crotches; leaves turn bronze, dry up, and drop."
        ),
        "favorable_conditions": "Hot (>30°C), dry, dusty conditions and drought-stressed plants.",
        "treatment": [
            "Spray with insecticidal soap, horticultural oil, or neem oil, thoroughly coating leaf undersides.",
            "Release predatory mites (e.g., Phytoseiulus persimilis or Neoseiulus californicus) in greenhouses.",
            "Apply miticides (e.g., bifenazate, abamectin) if infestations exceed commercial economic thresholds."
        ],
        "prevention": [
            "Avoid plant water stress: maintain adequate and consistent soil moisture.",
            "Hose down dusty farm paths or borders to reduce mite migration.",
            "Avoid broad-spectrum synthetic pyrethroids that destroy beneficial mite predators."
        ]
    },
    "Tomato___Target_Spot": {
        "display_name": "Tomato - Target Spot",
        "plant": "Tomato",
        "condition": "Target Spot",
        "status": "Diseased",
        "severity": "Moderate",
        "pathogen_type": "Fungal (Corynespora cassiicola)",
        "symptoms": (
            "Small pinpoint brown spots on leaves that enlarge to circular lesions with light brown centers "
            "and dark concentric margins. Lesions can also attack fruit, causing sunken firm craters."
        ),
        "favorable_conditions": "Warm temperatures (20-30°C) and high humidity or prolonged leaf wetness.",
        "treatment": [
            "Spray strobilurin or carboxamide fungicides (e.g., azoxystrobin, penthiopyrad) or chlorothalonil.",
            "Improve air movement by increasing plant spacing and pruning lower leaves.",
            "Remove diseased leaf debris promptly."
        ],
        "prevention": [
            "Do not grow tomatoes adjacent to old unharvested solanaceous crops.",
            "Stake and tie plants to keep fruit and leaves well off the ground.",
            "Water with subterranean drip lines."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "display_name": "Tomato - Tomato Yellow Leaf Curl Virus (TYLCV)",
        "plant": "Tomato",
        "condition": "Tomato Yellow Leaf Curl Virus",
        "status": "Diseased",
        "severity": "Critical",
        "pathogen_type": "Viral (Begomovirus, vectored by Silverleaf Whitefly Bemisia tabaci)",
        "symptoms": (
            "Severe upward curling and cupping of leaflets, chlorosis (yellowing) of leaf margins, "
            "pronounced plant stunting, bushy erect growth habit, and almost complete flower drop."
        ),
        "favorable_conditions": "Warm arid or tropical seasons when silverleaf whitefly populations surge.",
        "treatment": [
            "Infected plants cannot be cured; remove and bag infected plants immediately to prevent whitefly vectoring.",
            "Control whiteflies using reflective silver mulches, yellow sticky cards, and systemic insect control (imidacloprid or dinotefuran).",
            "Spray insecticidal soaps or horticultural oils to suppress nymph stages."
        ],
        "prevention": [
            "Plant TYLCV-resistant tomato cultivars (e.g., Tygress, Charger, Invictus).",
            "Cover young seedlings in nurseries with 50-mesh insect-proof netting.",
            "Eradicate weed hosts (black nightshade, jimsonweed) around field borders."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "display_name": "Tomato - Tomato Mosaic Virus (ToMV)",
        "plant": "Tomato",
        "condition": "Tomato Mosaic Virus",
        "status": "Diseased",
        "severity": "High",
        "pathogen_type": "Viral (Tobamovirus, mechanically transmitted)",
        "symptoms": (
            "Mottling of leaves with alternating light and dark green mosaic patterns. "
            "Leaves may become distorted, curled, narrow ('shoestring' or 'fern-leaf' appearance), with stunted growth."
        ),
        "favorable_conditions": "Easily transmitted through human hands, tools, grafting, and contaminated tobacco products.",
        "treatment": [
            "No chemical cure exists. Immediately rogued out and destroy infected plants.",
            "Wash hands thoroughly with soap or 20% non-fat dry milk solution before handling tomato plants.",
            "Disinfect pruning shears and stakes in a 10% household bleach or trisodium phosphate (TSP) solution."
        ],
        "prevention": [
            "Plant certified ToMV-resistant cultivars (indicated by 'T' or 'ToMV' designation on seed packets).",
            "Prohibit smoking or chewing tobacco anywhere near tomato greenhouses or gardens.",
            "Soak seeds in 10% trisodium phosphate for 15 minutes before sowing."
        ]
    },
    "Tomato___healthy": {
        "display_name": "Tomato - Healthy Foliage",
        "plant": "Tomato",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "pathogen_type": "None",
        "symptoms": "Vigorous, dark green compound foliage with strong stems, uniform leaflets, and healthy flower trusses.",
        "favorable_conditions": "Full sun (6-8 hours daily), warm days (21-29°C), rich well-drained organic soil, and steady watering.",
        "treatment": [
            "No disease treatment required.",
            "Maintain routine sucker pruning to focus plant energy on primary fruit trusses.",
            "Feed bi-weekly with organic tomato food (high potassium, moderate nitrogen, plus calcium)."
        ],
        "prevention": [
            "Stake or cage securely to support heavy fruit clusters.",
            "Apply straw or organic mulch to retain uniform moisture and prevent blossom end rot.",
            "Water deeply at the base early in the day."
        ]
    }
}


from functools import lru_cache


@lru_cache(maxsize=128)
def get_disease_info(raw_class_name: str) -> dict:
    """
    Retrieve disease information by raw class name with LRU in-memory caching.
    Subsequent lookups for the same class execute in ~0.0ms.
    If not found, returns a safe fallback dictionary.
    """
    if raw_class_name in DISEASE_DATABASE:
        return DISEASE_DATABASE[raw_class_name]

    # Friendly parsing fallback if raw class name slightly differs
    parts = raw_class_name.split("___")
    plant = parts[0].replace("_", " ").title() if len(parts) > 0 else "Unknown Plant"
    condition = parts[1].replace("_", " ").title() if len(parts) > 1 else "Condition"
    is_healthy = "healthy" in raw_class_name.lower()

    return {
        "display_name": f"{plant} - {condition}",
        "plant": plant,
        "condition": condition,
        "status": "Healthy" if is_healthy else "Diseased",
        "severity": "None" if is_healthy else "Moderate",
        "pathogen_type": "None" if is_healthy else "Unspecified Pathogen",
        "symptoms": "Refer to agricultural extension services for specific lesion patterns and diagnostic tests.",
        "favorable_conditions": "Varies by specific microclimate and environmental stresses.",
        "treatment": [
            "Isolate the plant or affected branch to prevent potential transmission.",
            "Consult local agronomic extension guidelines for recommended cultural or chemical controls."
        ],
        "prevention": [
            "Practice proper crop rotation and sanitation.",
            "Maintain adequate spacing and balanced soil fertilization."
        ]
    }


@lru_cache(maxsize=1)
def get_all_disease_profiles() -> dict:
    """Return the entire disease database with cached reference."""
    return DISEASE_DATABASE


@lru_cache(maxsize=1)
def get_unique_crops() -> list:
    """Return sorted list of unique host plant crops cached in memory."""
    return sorted(list(set(d["plant"] for d in DISEASE_DATABASE.values())))

