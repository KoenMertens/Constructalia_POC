import streamlit as st

# Pagina instellingen
st.set_page_config(page_title="ArcelorMittal Constructalia POC Bot", layout="centered")

# Custom CSS voor een strakke 'show' (geen icons/symbols)
st.markdown("""
<style>
    .stChatMessage { background-color: #f0f2f6; border-radius: 10px; padding: 10px; margin-bottom: 10px; }
    .stChatInputContainer { padding-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("Constructalia Product Expert POC")
st.write("Please ask only those questions you provided, this is just a POC...")

# De verzamelde data van je vragen
KNOWLEDGE_BASE = {
    "What is XCarb?": """According to the official information from ArcelorMittal's Constructalia website, XCarb® is an umbrella brand that brings together all of ArcelorMittal’s reduced, low, and zero-carbon steel making activities, as well as wider initiatives and green innovation projects.
Its goal is to achieve the company's commitment to reach net-zero carbon emissions by 2050. It consists of three main initiatives:
XCarb® green steel certificates: These certificates allow customers to report a reduction in their Scope 3 carbon emissions.
They are backed by actual CO2 savings achieved through ArcelorMittal's decarbonization investments (e.g., Smart Carbon or innovative technologies).
XCarb® recycled and renewably produced: This label applies to products made via the Electric Arc Furnace (EAF) route using 100% scrap and 100% renewable electricity.
This process results in steel with a significantly lower CO2 footprint (as low as 300kg of CO2 per tonne of finished product).
XCarb® innovation fund: ArcelorMittal invests in companies developing breakthrough technologies that will accelerate the transition to carbon-neutral steelmaking.
Source / More Information:
You can find the detailed explanation and further tools related to these initiatives on the official Constructalia page:
Constructalia - XCarb® Green Steel Certificates
Constructalia - Sustainability / XCarb (General sustainability overview including XCarb products)""",

    "Where can I find the EPD for organic coated steel?": """To find the Environmental Product Declaration (EPD) for organic coated steel on the ArcelorMittal Constructalia website, you should follow these specific steps to ensure you get the most accurate and up-to-date document.
Where to find it:
Navigate to the Tool & Services section: Go to the official website at constructalia.arcelormittal.com.
Look for "Environmental Product Declarations": You can find a dedicated section for EPDs under the "Sustainability" or "Tools & Services" menu.
Specific Product Search: ArcelorMittal categorizes EPDs by product family. For organic coated steel, you are likely looking for the Granite® or Estetic® product ranges.
Direct Links to Relevant EPDs:
ArcelorMittal has several EPDs for organic coated steel depending on the production route (Standard vs. XCarb®):
Standard Organic Coated Steel (Granite® & Estetic®): This EPD covers 1m² of organic coated steel from the standard production route.
Download Standard Organic Coated Steel EPD (Verified via IBU - Institut Bauen und Umwelt e.V.)
XCarb® Recycled and Renewably Produced Organic Coated Steel: If you are looking for the low-carbon version (made via EAF with 100% renewable electricity), there is a specific EPD for this.
Download XCarb® Organic Coated Steel EPD
Key Details for Correctness:
Validity: The current EPD for standard organic coated steel (Granite®/Estetic®) is typically valid for 5 years.
Always check the "Valid to" date on the cover page (the latest version is generally valid until November 2024 or has been recently updated to 2029).
Standard: Ensure the document mentions compliance with EN 15804 and ISO 14025, which are the European and International standards for EPDs.
Search Tip: If you cannot find the direct link on Constructalia's main page, use their Product Catalogue search, where EPDs are often attached as technical downloads for specific steel grades like Granite®.""",

    "What is Angelina?": """Angelina® is a structural steel beam characterized by its unique sinusoidal (wave-like) web openings.
It is a type of "cellular beam" or "castellated beam" created through a patented process:
Fabrication: A standard hot-rolled I-section beam is cut along its web in a wave-like (sinusoidal) line.
The two resulting T-sections are then shifted and re-welded together at the peaks.
Result: This process increases the height of the beam without adding significant weight, resulting in a structural element with a very high strength-to-weight ratio and a distinctive aesthetic look.
Where can you use it?
Angelina® beams are primarily used to create long, column-free spans while allowing building services to pass through the beam itself.
Key applications include:
Floors & Offices: Because technical installations (MEP: pipes, ducts, and electrics) can pass through the sinusoidal openings, floor-to-floor height can be reduced, often allowing for an extra floor in height-restricted buildings.
Roofing Systems: Ideal for spans of 20m to 40m, providing a lightweight alternative to traditional trusses.
Car Parks: The openings improve natural light and ventilation, and the beams are often used in combination with long-span floor systems like Cofraplus 220.
Renovations: Their light weight and aesthetic appeal make them suitable for modernizing and strengthening existing architectural structures.
Footbridges & Gangways: Used where a combination of high load-bearing capacity and a sleek, transparent appearance is required.
Official Links & Resources
To find more details on the Constructalia/ArcelorMittal sites, you can use these links:
Official Angelina® Product Page: General overview and case studies.
Technical Brochure (PDF): A deep dive into the technical specifications, fabrication, and design principles (from ArcelorMittal Projects).
Constructalia - Cellular Beams Section: Direct product section for ACB® and Angelina® beams on the Constructalia platform.
Software Tool: ANGELINA: ArcelorMittal provides free design software to help engineers calculate the optimal beam geometry.""",

    "What low carbon steel products does ArcelorMittal offer for the construction market?": """ArcelorMittal's low-carbon steel for construction is grouped under the XCarb brand.
The offering is primarily split into physical products with a low CO2 footprint and certificates for carbon savings.
XCarb Recycled and Renewably Produced These are physical steel products made in an Electric Arc Furnace (EAF) using high levels of scrap and 100 percent renewable electricity.
They have a carbon footprint as low as 300kg per tonne of steel.
Structural Sections: I-sections, H-sections, and channels used for building frames.
Merchant Bars: Small sections used in light construction and finishing.
Sheet Piling (EcoSheetPile Plus): The world's first low-carbon sheet pile range for foundations and civil engineering.
Reinforcing Steel (Rebar): Steel used for concrete reinforcement.
Coated Steels: -- Granite and Estetic: Organic coated steels for facades and roofing.
-- Magnelis: A metallic coating that offers superior corrosion protection for solar structures and harsh environments.
Direct URL to Product Overview: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced
XCarb Green Steel Certificates These certificates allow construction customers to buy the green value of ArcelorMittal's decarbonization investments.
They are typically used for flat steel products produced via the traditional blast furnace route to help reduce the project's Scope 3 emissions.
Direct URL to Certificate Details: https://constructalia.arcelormittal.com/en/tools-and-services/xcarb-green-steel-certificates
Specialized Low-Carbon Solutions
EcoSheetPile Plus: Specific page for sustainable foundation solutions. https://constructalia.arcelormittal.com/en/products/ecosheetpile-plus
Sustainability Hub: The central page for all environmental information, including EPDs (Environmental Product Declarations) for these products. https://constructalia.arcelormittal.com/en/sustainability
Steligence: A holistic approach to building design that uses high-strength and low-carbon steel to reduce the overall material used in a building.
https://constructalia.arcelormittal.com/en/steligence""",

    "What roofing solutions are shown on Constructalia?": """1. Principal Roofing Systems
These are the main categories of roof constructions offered for industrial, commercial, and residential buildings:
Single Skin Profiles: These are cold-formed steel sheets used for simple roof coverings or as the outer layer of a built-up system.
Sandwich Panels (Promisol and Ondatherm): Pre-fabricated elements consisting of two steel skins with an insulating core (usually PIR or mineral wool), providing excellent thermal performance and quick installation.
Built-up Systems (Globalroof): A multi-layer system comprising a structural tray, insulation, and an outer profile, allowing for high acoustic and thermal customization.
Standing Seam Roofs (Mauka Line): A premium aesthetic solution with hidden fixings, ideal for contemporary architecture and low-pitched roofs.
Direct URL to Roof Applications Overview: https://constructalia.arcelormittal.com/en/applications/envelope/roofs
2. Structural Roofing Components
These products provide the structural strength required to support the roof envelope:
Roofing Trays (Globaldeck): Structural steel trays that span between the main frames to support insulation and waterproofing.
Purlins and Rails (Multibeam): Cold-rolled galvanized profiles that act as the secondary structure to support the roof cladding.
Arval Roof Profiles: A wide range of trapezoidal and sinusoidal profiles for various spanning requirements.
Direct URL to Arval (Envelope) Products: https://constructalia.arcelormittal.com/en/products/arval-envelope-solutions
3. Specialized and Low-Carbon Roofing
Magnelis for Roofs: A metallic coating (Zinc-Aluminum-Magnesium) that provides extreme corrosion resistance, often used for roofs in harsh or coastal environments.
XCarb Recycled and Renewably Produced Roofing: Low-carbon versions of roofing profiles and panels made with 100 percent renewable electricity and recycled steel.
Direct URL to XCarb Construction Products: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced
4. Design Tools for Roofing
Constructalia also provides software to help engineers and architects design these roof systems:
Roofing and Cladding Selector: A tool to choose the right profile based on span and load.
Span Tables: Technical data for the load-bearing capacity of various roof sheets.
Direct URL to Tools and Services: https://constructalia.arcelormittal.com/en/tools-and-services""",

    "Which product has the highest corrosion resistance?": """According to the official ArcelorMittal Constructalia and technical documentation, the product with the highest and most advanced corrosion resistance is Magnelis.
What is Magnelis? Magnelis is an exceptional metallic coating composed of Zinc, 3.5 percent Aluminium, and 3 percent Magnesium.
While standard galvanization uses pure zinc, the addition of 3 percent magnesium is the key factor that creates a significantly more stable and durable protective layer.
Why it has the highest resistance:
Up to 10 times better than galvanized steel: In salt spray tests, Magnelis outperforms standard hot-dip galvanized steel by a factor of 10.
Self-healing protection: It is famous for its self-healing properties. When the steel is cut or scratched, the magnesium-rich layer migrates to cover the exposed edge, preventing red rust from forming.
Harsh Environments: It is the best choice for highly alkaline environments and environments containing ammonia (such as agricultural buildings) or chlorides (coastal areas or swimming pools).
Longevity: It can provide a service life of up to 20 to 25 years even in the most demanding conditions (C5 corrosion category).
Specific Grade with Highest Resistance: The Magnelis ZM620 grade (offering 620g per square meter of coating) is the most robust version, specifically designed for structures with extreme requirements, such as ground-mounted or floating solar plants.
Official Links on Constructalia and ArcelorMittal:
Magnelis Product Page (General Overview): https://constructalia.arcelormittal.com/en/products/magnelis
Sustainability and Magnelis (Environmental details): https://constructalia.arcelormittal.com/en/sustainability
Technical Information on Corrosion Protection: https://constructalia.arcelormittal.com/en/tools-and-services/technical-documentation
Detailed Case Study on ZM620 (Extreme resistance for Solar): https://corporate.arcelormittal.com/media/cases-studies/twice-as-nice-arcelormittal-adds-new-steel-grade-to-its-portfolio
Note for Marine Environments: For heavy civil engineering and foundations specifically in sea water, ArcelorMittal also offers AMLoCor, which is a low-corrosion steel grade designed for marine sheet piling.
However, for general construction and coated products, Magnelis remains the industry leader for corrosion resistance.""",

    "What are the technical properties of Granite?": """The technical properties of Granite® organic coated steel from ArcelorMittal vary depending on the specific product line (such as Standard, HD, HDX, or HDXtreme).
However, they generally follow a standard technical framework for building and construction.
1. Core Material and Substrate
Substrate: Hot-dip galvanized steel (Z), Galfan (ZA), or Zinc-Aluminium-Magnesium (ZM) like Magnelis.
Substrate Grade: Typically Z225 to Z275 (grams per square meter) or equivalent, providing initial corrosion protection.
Sustainability: Part of the Nature range, meaning it is free of hexavalent chromium and heavy metals (Lead, Mercury, Cadmium) and is fully REACH compliant.
2. Coating Performance and Durability
Coating Thickness: Ranges from 25 microns (Granite Standard/HD) to 55 microns (Granite HDX) and up to 75 microns (Granite HDXtreme).
Corrosion Resistance Category (RC): Rated from RC3 (Standard) up to RC5 or RC5 plus (HDX and HDXtreme) according to EN 10169.
UV Resistance Category (RUV): Rated from RUV3 to RUV4, and RUV5 for the highest-performing versions (HDXtreme), ensuring color stability and gloss retention even in high-sunlight regions.
3. Mechanical and Forming Properties
Formability (T-bend): Typically less than or equal to 1T or 1.5T for adhesion and 2T for cracking, allowing the steel to be bent and profiled without damaging the paint.
Clemen Scratch Resistance: Usually 2 kg to 3 kg or higher for textured versions, making the surface robust during handling and installation.
Impact Resistance: Standardized at 18 Joules.
Pencil Hardness: Typically HB to H.
4. Thermal and Fire Behavior
Fire Classification: Rated A1 (non-combustible) according to EN 13501-1 for most standard colors.
Temperature Resistance: Can withstand continuous operating temperatures up to 100 degrees Celsius.
5. Aesthetic Properties
Gloss Levels: Standard gloss is 30 GU (Gloss Units), but options range from Ultra Matt (under 5 GU) to High Gloss (over 80 GU).
Finishes: Available in smooth, grained, wrinkled, or mineral-textured (Quartz) appearances.
Technical Links for Verification:
You can find the detailed datasheets and brochures for each specific Granite product at these full URLs:
Granite HDX Technical Datasheet: https://constructalia.arcelormittal.com/en/products/granite-hdx
Granite Product Range Overview:https://constructalia.arcelormittal.com/en/products/granite
Technical Documentation Center:https://constructalia.arcelormittal.com/en/tools-and-services/technical-documentation""",

    "What is SiCA?": """Based on the ArcelorMittal Constructalia website, SiCA stands for Sustainable Industrial Construction Assistant.
It is a specialized digital tool and methodology developed by ArcelorMittal to evaluate and compare the environmental and economic impact of different structural solutions for industrial buildings (such as warehouses or logistics centers) from a Life Cycle Assessment (LCA) perspective.
Key functions of SiCA:
Comparative Analysis: It allows engineers and architects to compare traditional construction methods with optimized steel-based solutions.
Environmental Impact: It calculates the Global Warming Potential (GWP) and other environmental indicators (embodied carbon) of a building's structure.
Economic Evaluation: It provides a "Total Cost of Ownership" perspective, considering not just initial material costs but also construction speed and long-term durability.
Optimization: It helps users choose the most sustainable and cost-effective combination of products (such as XCarb® steel, Magnelis® coatings, or specific roofing systems).
Official Links on Constructalia:
To ensure you can copy and paste the links easily, I have provided the full URLs below:
SiCA Tool and Methodology Page: https://constructalia.arcelormittal.com/en/tools-and-services/sica-sustainable-industrial-construction-assistant
Sustainability Tools Overview: https://constructalia.arcelormittal.com/en/sustainability
Case Studies using SiCA: https://constructalia.arcelormittal.com/en/case-studies
(Note: Access to the full SiCA software tool typically requires a login or a request for a consultant-led study via the ArcelorMittal technical team.)""",

    "How many lessons are there in SiCA?": """Based on the ArcelorMittal Constructalia website, SiCA (Sustainable Industrial Construction Assistant) is organized into 5 lessons.
These lessons are designed to guide the user through the methodology and use of the tool to optimize industrial building projects.
The 5 lessons are:
Lesson 1: Introduction and context
Lesson 2: The tool and the methodology
Lesson 3: Environmental assessment (LCA)
Lesson 4: Economic assessment (LCC)
Lesson 5: Practical application and case studies
You can find this information on the official Constructalia page dedicated to the SiCA tool:
Direct URL to SiCA: https://constructalia.arcelormittal.com/en/tools-and-services/sica-sustainable-industrial-construction-assistant
Direct URL to the SiCA e-learning/course section: https://constructalia.arcelormittal.com/en/tools-and-services/sica-sustainable-industrial-construction-assistant/lessons
(Note: You may need to be logged in to the Constructalia platform to view the specific content of each lesson in detail.)""",

    "Example case studies with solutions for high-rise buildings": """Based on the ArcelorMittal Constructalia website, high-rise and multi-storey building case studies focus on structural efficiency, speed of construction, and the use of high-strength steel.
To ensure you can copy and paste the information easily, I have provided the names of notable case studies and their full web addresses without any symbols or icons.
1. Notable High-Rise Case Studies
Hines Panorama (Warsaw, Poland): This 160-meter high skyscraper used high-strength steel sections (HISTAR) to reduce the weight of the structure and optimize floor space.
D2 Tower (Paris La Défense, France): An iconic high-rise with an external steel exoskeleton (diagrid), which allowed for column-free interior spaces and a unique aesthetic.
One World Trade Center (New York, USA): While a global landmark, it is featured for its use of high-performance steel to ensure safety and structural integrity.
Caleido Tower (Madrid, Spain): A multi-storey project that utilized a mixed steel-concrete structure to achieve rapid construction in a dense urban area.
2. Common Solutions for High-Rise Buildings
According to the site, these buildings typically utilize the following technical solutions:
HISTAR (High-Strength Steel): Used in columns to carry heavy loads with smaller sections, maximizing rentable floor area.
Coils and Sheets for Composite Floors: Systems like Cofraplus or Cofradal that provide lightweight floor solutions and serve as a working platform during construction.
Angelina Beams: Used for long spans and to facilitate the passage of technical services (HVAC, cables) through the web openings.
Steligence: A holistic design approach that combines high-strength steel and optimized engineering to reduce the carbon footprint and cost of tall buildings.
3. Official Links on Constructalia
You can browse the full list of case studies and filter by "Multi-storey buildings" or "Skyscrapers" using these URLs:
Case Studies Overview Page: https://constructalia.arcelormittal.com/en/case-studies
Steligence Solutions for Multi-Storey Buildings: https://constructalia.arcelormittal.com/en/steligence
Technical Documentation for High-Rise Structures: https://constructalia.arcelormittal.com/en/tools-and-services/technical-documentation
(Note: You can use the search bar on the Case Studies page to find specific projects like "D2 Tower" or "Hines Panorama" for deeper technical analysis.)""",

    "Which steel has the highest compressive strength?": """According to the ArcelorMittal Constructalia website and technical documentation, the steel products with the highest strength—specifically used to handle massive compressive loads in high-rise buildings and columns—are the HISTAR® grades and the Amstrong® Ultra range.
In structural steel, compressive strength is directly related to the yield strength (the stress level where the material begins to deform).
1. HISTAR® (For High-Rise Columns)
HISTAR® is specifically marketed for its ability to support the weight of skyscrapers.
It is often referred to as the "gravity column" solution because it allows for smaller, high-capacity columns that maximize rentable floor space.
Highest Grade: HISTAR® 460 (Yield strength of 460 MPa).
Recent Developments: New technical approvals (like ETA-10/0156) allow for even higher performance grades like S500, S600, and S700 in specific rolled sections to carry even greater compressive loads.
2. Amstrong® Ultra (For Extreme High-Strength Applications)
For specialized construction and industrial applications (though less common for standard building frames than HISTAR), ArcelorMittal offers the Amstrong® Ultra range of quenched and tempered steels.
These have significantly higher strength values:
Amstrong® Ultra 690 (Yield strength of 690 MPa).
Amstrong® Ultra 960 (Yield strength of 960 MPa).
3. Key Advantages for Compression
Weight Saving: Using high-strength steel like HISTAR 460 instead of standard S355 can reduce the weight of a column by up to 30 to 40 percent.
Space Optimization: Higher compressive strength means the columns can be thinner while supporting the same load, which is critical in the lower floors of high-rise buildings.
Official Links on Constructalia:
To ensure you can copy and paste the links easily, I have provided the full URLs below:
HISTAR® Product Overview:https://constructalia.arcelormittal.com/en/products/histar
High Strength Steels (Amstrong® range):https://industeel.arcelormittal.com/product/high-strength-steels/
Technical Brochure for High-Rise Buildings (Section on Columns):https://constructalia.arcelormittal.com/en/tools-and-services/technical-documentation
Case Study: D2 Tower (Using high-strength steel for compression):https://constructalia.arcelormittal.com/en/case-studies/d2-tower-la-defense
(Note: In the search for "compressive strength" on Constructalia, you will find it primarily discussed in the context of "columns" and "multi-storey buildings" where high-strength steel grades like HISTAR 460 are the standard recommendation.)""",

    "What is the biggest benefit of xcarb offer? (specialnie z małymi literami)": """Based on the ArcelorMittal Constructalia website, the biggest benefit of the xcarb (XCarb) offer is that it brings together all of ArcelorMittal’s reduced, low, and zero-carbon steel making activities into a single initiative to help customers significantly reduce their Scope 3 carbon emissions.
By using products from the xcarb range, specifically the recycled and renewably produced line, customers can reduce the carbon footprint of their steel projects by up to 70 percent compared to the industry average.
The main benefits identified on the site are:
Significant reduction in embodied carbon: The recycled and renewably produced steel has a CO2 footprint as low as 300kg per tonne of finished steel.
Official reporting: It allows customers to report reductions in their indirect emissions (Scope 3) in accordance with the Greenhouse Gas (GHG) Protocol.
Transparency: Every product is backed by a specific Environmental Product Declaration (EPD) or an official certificate.
Future-proofing: It provides a clear pathway toward the goal of carbon-neutral steel by 2050.
Official Links on Constructalia:
XCarb Sustainability Overview: https://constructalia.arcelormittal.com/en/sustainability
XCarb Recycled and Renewably Produced: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced
XCarb Green Steel Certificates: https://constructalia.arcelormittal.com/en/tools-and-services/xcarb-green-steel-certificates
Steligence ad Carbon Reduction: https://constructalia.arcelormittal.com/en/steligence""",

    "I want to build residential building. Which products do you offer me to use?": """Based on the ArcelorMittal Constructalia website, the products offered for residential buildings are categorized into structural systems, flooring, and envelope (facade and roof) solutions.
These products are designed to provide speed of construction, lightweight structures, and high aesthetic quality.
The following products and solutions are specifically recommended for the residential market:
Structural and Flooring Solutions
Cofraplus: Composite floor systems (such as Cofraplus 60 or 71) that act as stay-in-place formwork for concrete slabs, reducing weight and construction time.
Cofradal: A pre-fabricated composite floor system that offers high acoustic and thermal performance, which is essential for multi-family residential units.
Slim Floor (IFB/SFB Beams): Integrated floor beams that allow the floors to be "tucked into" the beam depth, resulting in a flat ceiling and reduced floor-to-floor height.
Angelina Beams: Sinusoidal web beams used for long spans and to easily integrate technical installations (pipes and ducts) within the floor depth.
Envelope and Facade Solutions (Arval)
Granite: A range of organic coated steels for durable and aesthetic facades and roofs, available in many colors and textures.
Mauka Line: A standing seam roofing system often used in residential architecture for its modern, clean look and excellent weather resistance.
Sinusoidal and Trapezoidal Profiles: Used for contemporary steel cladding on residential exteriors.
Sandwich Panels (Ondatherm and Promisol): Insulated panels that provide high thermal efficiency for the building shell.
Sustainability and Low Carbon Options
XCarb Recycled and Renewably Produced: Low-carbon steel versions of the beams and sections mentioned above, helping to reduce the overall environmental impact of the residential project.
Official Links on Constructalia:
Residential Applications Overview: https://constructalia.arcelormittal.com/en/applications/residential-buildings
Floor Systems (Cofraplus and Cofradal): https://constructalia.arcelormittal.com/en/products/composite-floors
Facade and Roofing Solutions (Arval): https://constructalia.arcelormittal.com/en/products/arval-envelope-solutions
XCarb for Construction: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced
Steligence for Residential Buildings: https://constructalia.arcelormittal.com/en/steligence""",

    "I need to design an office building. Which solutions would you recommend?": """Based on the ArcelorMittal Constructalia website, office building solutions are focused on maximizing floor space, ensuring flexibility for future changes, and providing high thermal and acoustic comfort.
The following solutions are recommended for designing an office building:
Structural and Floor Solutions
Angelina Beams: These sinusoidal web beams are ideal for office buildings because the openings allow for the easy integration of HVAC ducts, pipes, and cables within the floor depth.
This reduces the overall floor-to-floor height, potentially allowing for extra floors in a building of a given height.
Slim Floor (IFB and SFB Beams): Integrated Floor Beams allow the floor slab to sit on the bottom flange of the beam.
This creates a flat ceiling without visible beams, providing a clean aesthetic and maximum flexibility for office layouts.
Cofraplus and Cofradal: Composite floor systems that provide excellent acoustic insulation (essential for offices) and high load-bearing capacity while remaining lightweight.
HISTAR: High-strength steel sections used for columns to minimize their footprint, thereby increasing the usable and rentable office floor area.
Envelope and Facade Solutions
Granite: A range of prepainted steels for aesthetic facades, available in various finishes like Granite Silky Shine or Granite Quartz to give office buildings a premium look.
Promisol and Ondatherm: Insulated sandwich panels for walls that provide high thermal efficiency and airtightness, helping to reduce the building's energy consumption.
Sun-shading systems: Steel-based perforated sheets or mesh can be used for solar shading to improve occupant comfort and reduce cooling costs.
Holistic Design Approach
Steligence: ArcelorMittal’s science-based approach to building design. For offices, Steligence focuses on optimizing the structural weight, increasing flexibility for future interior reconfigurations, and improving the building's overall sustainability rating (BREEAM/LEED).
Official Links on Constructalia:
Office Buildings Application Overview: https://constructalia.arcelormittal.com/en/applications/offices
Angelina Beams for Offices: https://constructalia.arcelormittal.com/en/products/acb-and-angelina-beams
Floor Systems (Cofraplus and Cofradal): https://constructalia.arcelormittal.com/en/products/composite-floors
Steligence Approach for Offices: https://constructalia.arcelormittal.com/en/steligence
XCarb for Low Carbon Construction: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced""",

    "What is the most durable solution for silos?": """Based on the ArcelorMittal Constructalia website and official ArcelorMittal technical data, the most durable and cost-effective solution for silos is Magnelis®.
In addition to Magnelis, ArcelorMittal has launched a specific high-strength grade for enameled silos called S390 EK.
1. Magnelis (Corrosion Resistance)
Magnelis is considered the industry-leading solution for agricultural and industrial silos due to its extreme resistance to harsh environments.
Durability: It offers up to 10 times better corrosion resistance than standard hot-dip galvanized steel.
Self-Healing: Magnelis has a unique "self-healing" property where the magnesium-rich coating migrates over cut edges and scratches to prevent red rust.
Ammonia Resistance: It is highly resistant to alkaline environments and ammonia, making it ideal for the storage of grain and animal feed where traditional coatings fail.
Grades: For extreme durability, the ZM310 (310g/m2) coating is the standard recommendation for silos.
2. S390 EK (Mechanical Strength for Enamelling)
For silos that require an enameled finish (often used for liquid storage or specific chemicals), ArcelorMittal offers S390 EK.
Strength: It guarantees a minimum yield strength of 390 MPa after the enamel firing process, allowing for thinner and lighter silo walls.
Quality: It is specifically designed for two-sided enamelling to avoid "fish-scaling" (surface defects), which ensures a longer operational life for the tank.
Official Links on Constructalia:
To ensure you can copy and paste the links easily, here are the full URLs:
Magnelis Product Page:https://constructalia.arcelormittal.com/en/products/magnelis
Agriculture and Silos Solutions:https://constructalia.arcelormittal.com/en/applications/agriculture
Technical Data on Metallic Coatings:https://constructalia.arcelormittal.com/en/tools-and-services/technical-documentation
High Strength Steels for Industry (S390 EK):https://industry.arcelormittal.com/S390EK""",

    "Which product in ArcelorMittal's construction market offering has the lowest CO2 equivalent emissions?": """Based on the ArcelorMittal Constructalia website, the products with the lowest CO2 equivalent emissions are those belonging to the XCarb Recycled and Renewably Produced range.
The specific product with the lowest recorded carbon footprint is XCarb Recycled and Renewably Produced structural steel (such as beams and sections) and EcoSheetPile Plus.
Key facts regarding the lowest CO2 emissions:
Carbon Footprint: These products have a CO2 footprint as low as 300kg per tonne of finished steel.
Production Method: This is achieved by using an Electric Arc Furnace (EAF) with nearly 100 percent scrap steel and 100 percent renewable electricity.
Comparison: This represents a massive reduction compared to the traditional blast furnace route, which typically averages around 2,100kg of CO2 per tonne of steel.
Certification: The emissions are verified through product-specific Environmental Product Declarations (EPDs).
Official Links on Constructalia:
XCarb Recycled and Renewably Produced Product Page: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced
EcoSheetPile Plus (Low Carbon Foundations): https://constructalia.arcelormittal.com/en/products/ecosheetpile-plus
Sustainability Overview and EPDs: https://constructalia.arcelormittal.com/en/sustainability
XCarb Initiative Details: https://constructalia.arcelormittal.com/en/tools-and-services/xcarb-green-steel-certificates"""
}

# Chat logica
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hallo! I am the Constructalia expert. How can I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Typ your question (e.g. 'What is XCarb?')..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simpele keyword matching
    query = prompt.lower()
    response = "I can only answer those questions you provided for the moment, so I only provide information about XCarb, Angelina, Magnelis, Granite, SiCA, offices, construction, silo's and CO2 emission."
    
    for key, value in KNOWLEDGE_BASE.items():
        if key in query:
            response = value
            break

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
