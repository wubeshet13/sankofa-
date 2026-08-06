import os

# Single shared favicon — a clean "Z" monogram for Zemen Technologies
FAVICON = """<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='4' fill='%231c1917'/><text x='50%25' y='72%25' font-size='20' font-family='Georgia,serif' font-weight='700' fill='%23faf8f5' text-anchor='middle'>Z</text></svg>">"""

# Professional inline SVG icon library (stroke-based, neutral, no emojis)
ICONS = {
    "coffee":       '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 8h6a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2zm6 0V6a2 2 0 0 1 4 0v2M5 20h14"/></svg>',
    "grain":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2m0 14v2M3 12h2m14 0h2M5.6 5.6l1.4 1.4m9.9 9.9 1.4 1.4M5.6 18.4l1.4-1.4m9.9-9.9 1.4-1.4"/></svg>',
    "crane":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M2 20h20M6 20V10l6-6 6 6v10M10 20v-6h4v6"/></svg>',
    "truss":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 18 12 4l9 14H3zm4.5 0 4.5-7 4.5 7"/></svg>',
    "door":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><rect x="4" y="2" width="16" height="20" rx="1"/><circle cx="15" cy="12" r="1" fill="currentColor"/></svg>',
    "bolt":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/></svg>',
    "shirt":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 7l4-4h3a2 2 0 0 0 4 0h3l4 4-3 2v11H6V9L3 7z"/></svg>',
    "backpack":     '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 0 0-8 0v1H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2h-3V7zM9 7h6m-3 5v4m-2-2h4"/></svg>',
    "vest":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3 6 6v15h12V6l-6-3zm0 0v18"/></svg>',
    "truck":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M1 3h15v13H1zm15 4h4l3 3v6h-7V7zM5.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/></svg>',
    "box":          '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M20 7 12 3 4 7m16 0v10l-8 4m0-14L4 17m8-10v14M4 7l8 4"/></svg>',
    "clipboard":    '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2m-4 0a2 2 0 0 1 4 0m-4 0h4M9 12h6m-6 4h4"/></svg>',
    "needle":       '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="m4 20 16-16M4 20l6-2-4-4 2-6M15 5l4 4"/></svg>',
    "palette":      '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 2C6.48 2 2 6.48 2 12c0 4.42 3.58 8 8 8 .83 0 1.5-.67 1.5-1.5 0-.39-.15-.74-.39-1.01C10.89 16.99 11 16.51 11 16c0-1.1.9-2 2-2h2c2.76 0 5-2.24 5-5 0-4.42-3.58-8-8-8z"/><circle cx="6.5" cy="11.5" r="1.5" fill="currentColor" stroke="none"/><circle cx="9.5" cy="7.5" r="1.5" fill="currentColor" stroke="none"/><circle cx="14.5" cy="7.5" r="1.5" fill="currentColor" stroke="none"/><circle cx="17.5" cy="11.5" r="1.5" fill="currentColor" stroke="none"/></svg>',
    "interior":     '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9zm6 13V12h6v10"/></svg>',
    "scales":       '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v18m0 0H6m6 0h6M3 9l9-3 9 3M3 9l3 6a3 3 0 0 0 6 0L9 9m6 0 3 6a3 3 0 0 0 6 0l-3-6"/></svg>',
    "building":     '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 21V7l9-4 9 4v14M3 21h18M9 21V11h6v10M9 11h6"/></svg>',
    "contract":     '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h4M5 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm3 3h8"/></svg>',
    "solar":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2m0 14v2M3 12H1m22 0h-2m-3.2-6.8-1.4 1.4M7.6 16.4l-1.4 1.4m12.2 0-1.4-1.4M7.6 7.6 6.2 6.2"/><circle cx="12" cy="12" r="4"/></svg>',
    "battery":      '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M7 7h10a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2zm10 0V5h2v2M7 12h5"/></svg>',
    "chart":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 3v18h18M7 16l4-4 4 4 4-4"/></svg>',
    "shield":       '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3 4 7v6c0 5.25 3.75 10.15 8 11 4.25-.85 8-5.75 8-11V7l-8-4z"/></svg>',
    "broom":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="m3 21 7-7m0 0 6.5-6.5M10 14 4 9l7-7 5 5M13.5 7.5l3 3L21 6l-4-4-3.5 5.5z"/></svg>',
    "facility":     '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 21h18M3 7h18M3 14h18M9 3v18M15 3v18"/></svg>',
    "gate":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 3h8v18H3zm10 0h8v18h-8zM3 12h8m10 0h-8"/></svg>',
    "stair":        '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3 21h4v-4h4v-4h4v-4h4v-4h2"/></svg>',
    "grid":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
    "bowl":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M4 11a8 8 0 0 0 16 0H4zm8 9v-1m0 0a9 9 0 0 1-9-9h18a9 9 0 0 1-9 9zm-5-9V6a5 5 0 0 1 10 0v5"/></svg>',
    "pepper":       '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 2c1 0 2 .5 2 2 0 1-1 2-2 3-2 2-3 5-3 8a5 5 0 0 0 10 0 9 9 0 0 0-2-5.5"/><path stroke-linecap="round" stroke-linejoin="round" d="M14 4c2-1 4 0 4 2"/></svg>',
    "seed":         '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 22V12m0 0c0-4-3-8-8-8 0 5 3 8 8 8zm0 0c0-4 3-8 8-8 0 5-3 8-8 8z"/></svg>',
}

# Companies list
companies = [
    {
        "key": "akid-trading",
        "name": "Akid Trading PLC",
        "primary": "#854d0e",
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Connecting Global Commodities & Industrial Markets",
        "description": "Akid Trading PLC specializes in agricultural commodities exports and industrial machinery imports in Ethiopia.",
        "services": [
            {"title": "Coffee Export Division", "icon": "coffee", "desc": "Sourcing and exporting high-grade single-origin green Arabica coffee beans to global markets."},
            {"title": "Oilseeds & Pulses", "icon": "grain", "desc": "Supplying quality sesame seeds, soybeans, and chickpeas to international distributors."},
            {"title": "Industrial Materials Import", "icon": "crane", "desc": "Importing construction materials and manufacturing components for local industries."}
        ],
        "about": "Akid Trading PLC is a trade partner in agricultural exports and industrial imports. We prioritize quality control and reliable logistics transit to meet international standards.",
        "phone": "+251 929 906 501 / +251 996 181 818 / +251 911 823 482",
        "email": "info@akidtrading.com",
        "form_fields": ["Company Name", "Product Line of Interest", "Target Quantity (Tons)"]
    },
    {
        "key": "nuriye-netsanet-metal",
        "name": "Nuriye Netsanet & Friends Metal Works",
        "primary": "#7c2d12",
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Industrial Steel Fabrication & Structural Fitting",
        "description": "Nuriye Netsanet and Friends Metal Works specializes in the fabrication and installation of structural steel frameworks and heavy iron grids.",
        "services": [
            {"title": "Roof Steel Trusses", "icon": "truss", "desc": "Designing, welding, and installing structural steel roof trusses for industrial warehouses and buildings."},
            {"title": "Security Gates & Doors", "icon": "door", "desc": "Custom fabrication of secure compound sliding gates, security doors, and window grids."},
            {"title": "Structural Steel Fitting", "icon": "bolt", "desc": "On-site structural welding, beam alignment, and steel frame reinforcement for construction projects."}
        ],
        "about": "Nuriye Netsanet and Friends Metal Works provides metal welding and steel fabrication services in Ethiopia, focusing on structural integrity and design specifications.",
        "phone": "+251 911 455 992",
        "email": "info@nuriyemetal.com",
        "form_fields": ["Full Name / Contractor", "Fabrication Requirement", "Dimensions & Specifications"]
    },
    {
        "key": "meti-mekonnen-garment",
        "name": "Meti Mekonnen Garment",
        "primary": "#9f1239",
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Precision Tailoring & Bulk Uniform Manufacturing",
        "description": "Meti Mekonnen Garment manufactures school uniforms, corporate workwear, and safety attire using quality fabric blends.",
        "services": [
            {"title": "Corporate Apparel", "icon": "shirt", "desc": "Tailoring custom branded polo shirts, professional button-downs, and service uniforms."},
            {"title": "School Wear Packages", "icon": "backpack", "desc": "Complete uniform packages including school sweaters, skirts, trousers, and sports apparel."},
            {"title": "Industrial Safety Garments", "icon": "vest", "desc": "Durable safety overalls, high-visibility reflector vests, and lab coats for corporate operations."}
        ],
        "about": "Meti Mekonnen Garment provides apparel manufacturing services. We produce custom and bulk garments tailored for schools, corporate entities, and industrial worksites.",
        "phone": "+251 911 158 716",
        "email": "info@metigarments.com",
        "form_fields": ["Institution Name", "Uniform Type", "Estimated Order Volume"]
    },
    {
        "key": "daniel-tesfaye-freight",
        "name": "Daniel Tesfaye Dry Freight",
        "primary": "#1e3a8a",
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Cross-Border Dry Cargo Logistics",
        "description": "Daniel Tesfaye Freight operates cargo transport shipping on the Djibouti-Ethiopia logistics trade corridors.",
        "services": [
            {"title": "Djibouti Port Transit", "icon": "truck", "desc": "Dry container and bulk cargo transport from the Port of Djibouti to dry ports across central Ethiopia."},
            {"title": "Bulk Dry Cargo", "icon": "box", "desc": "Shipping bulk dry commodities including fertilizer, grains, and industrial raw minerals."},
            {"title": "Customs & Clearance Support", "icon": "clipboard", "desc": "Providing cargo transit tracking updates and cross-border transport logistics support."}
        ],
        "about": "Daniel Tesfaye Freight provides cargo transport services, prioritizing secure transit, schedule adherence, and dry freight shipping logistics.",
        "phone": "+251 903 336 633 / +251 973 077 878 / +251 911 246 272",
        "email": "info@danieldryfreight.com",
        "form_fields": ["Company Name", "Origin / Destination", "Cargo Weight (Tons)"]
    },
    {
        "key": "etege-design",
        "name": "Etege Design",
        "primary": "#581c87",
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Creative Identity Branding & Couture Fashion Curation",
        "description": "Etege Design specializes in visual branding layouts, artisanal couture design, and interior style curation.",
        "services": [
            {"title": "Artisanal Habesha Couture", "icon": "needle", "desc": "Designing traditional dresses featuring handwoven cotton textures and bespoke patterns."},
            {"title": "Creative Brand Identity", "icon": "palette", "desc": "Building custom brand books, corporate identities, logos, and product packaging layouts."},
            {"title": "Bespoke Interior Curation", "icon": "interior", "desc": "Curating hand-crafted textiles, clay decor elements, and custom furnishings for spaces."}
        ],
        "about": "Etege Design curates traditional Ethiopian design assets and artisanal garments. We collaborate with local handweavers and creators to deliver creative branding projects.",
        "phone": "+251 912 270 394 / +251 967 001 655",
        "email": "info@etegedesign.com",
        "form_fields": ["Client / Brand Name", "Design Scope", "Estimated Project Timeline"]
    },
    {
        "key": "dablo-law-firm",
        "name": "DABLO Law Firm LLP",
        "primary": "#1c3d5a",
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Legal Counsel & Business Advocacy Services",
        "description": "DABLO Law Firm LLP provides legal advisory, corporate compliance counsel, and litigation support in Ethiopia.",
        "services": [
            {"title": "Corporate & Business Law", "icon": "scales", "desc": "Legal advice on foreign direct investment, company formation, and regulatory compliance in Ethiopia."},
            {"title": "Commercial Litigation", "icon": "building", "desc": "Legal representation and advocacy in arbitration, commercial contract disputes, and tax matters."},
            {"title": "Contracts & Due Diligence", "icon": "contract", "desc": "Drafting commercial agreements, joint venture contracts, and conducting asset due diligence reviews."}
        ],
        "about": "DABLO Law Firm LLP provides commercial, tax, and investment legal services. We focus on protecting corporate interests and delivering advocacy solutions for business operations.",
        "phone": "+251 938 888 887 / +251 938 888 886 / +251 911 256 382",
        "email": "info@dablolaw.com",
        "form_fields": ["Client / Company Name", "Legal Area of Interest", "Urgency Level"]
    },
    {
        "key": "bright-africa",
        "name": "Bright Africa",
        "primary": "#065f46",
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Smart Renewable Solar Energy & Tech Systems",
        "description": "Bright Africa deploys high-efficiency solar grid installations, energy backup storage, and technology solutions.",
        "services": [
            {"title": "Smart Solar PV Arrays", "icon": "solar", "desc": "Designing and installing smart solar PV panels tailored for electrical power generation."},
            {"title": "Grid Battery Storage", "icon": "battery", "desc": "Deploying backup battery systems to provide stable, clean off-grid electrical power."},
            {"title": "Smart Energy Analytics", "icon": "chart", "desc": "Deploying smart energy meters and digital monitoring tools to track power load profiles."}
        ],
        "about": "Bright Africa is a technology-driven renewable energy firm. We focus on deploying sustainable solar energy systems and microgrids for commercial buildings, businesses, and communities.",
        "phone": "+251 913 937 219",
        "email": "info@brightafrica.net",
        "form_fields": ["Facility Name", "Average Monthly Power Bill (ETB)", "Available Roof Area (sqm)"]
    },
    {
        "key": "checkpoint-security",
        "name": "Check Point Security & Cleaning",
        "primary": "#1e3a8a",
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Corporate Guard Force & Facility Janitorial Services",
        "description": "Check Point Security and Cleaning Service PLC provides facility security guards and commercial janitorial cleaning solutions.",
        "services": [
            {"title": "Security Guard Force", "icon": "shield", "desc": "Deploying security guard teams for corporate offices, commercial areas, and manufacturing sites."},
            {"title": "Corporate Janitorial Cleaning", "icon": "broom", "desc": "Standard office cleaning schedules, floor polishing, window washing, and office sanitization services."},
            {"title": "Property Facility Support", "icon": "facility", "desc": "Providing minor facility checks, garbage management, landscaping, and maintenance support."}
        ],
        "about": "Check Point Security & Cleaning Service PLC provides guard deployment and commercial janitorial services, focusing on facility safety, cleanliness, and security standards.",
        "phone": "+251 933 525 155 / +251 911 459 477 / +251 911 792 268",
        "email": "info@checkpointsecurity.com",
        "form_fields": ["Organization Name", "Service Requirement", "Guards Required / Area (sqm)"]
    },
    {
        "key": "desalegn-metal",
        "name": "Desalegn & Friends Metal Work",
        "primary": "#451a03",
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Ornamental Residential Gates & Balcony Rails",
        "description": "Desalegn And Friends Metal Work fabricates custom entrance gates, balcony handrails, spiral stairs, and window security grids.",
        "services": [
            {"title": "Decorative Entry Gates", "icon": "gate", "desc": "Welding and painting compound swing gates, sliding steel gates, and security steel panels."},
            {"title": "Staircases & Balustrades", "icon": "stair", "desc": "Welding spiral stair structures and balcony handrail assemblies for residential properties."},
            {"title": "Security Window Grills", "icon": "grid", "desc": "Fabricating security steel grids to custom window sizes, offering home protection with clean designs."}
        ],
        "about": "Desalegn And Friends Metal Work specializes in domestic steel fabrications, cooperating with homeowners to design secure, durable, and functional metal elements.",
        "phone": "+251 913 552 420 / +251 911 321 010",
        "email": "info@desalegnmetal.com",
        "form_fields": ["Owner Name", "Fabrication Choice", "Dimensions Description"],
        "active": True,
        "expiry_date": "2026-07-27"
    },
    {
        "key": "priem-dry-food",
        "name": "Priem Dry Food Preparation PLC",
        "primary": "#9a3412",
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Hygienically Processed Spices & Premixed Shiro Pulses",
        "description": "Priem Dry Food Preparation PLC processes spices, ground hot pepper (Berbere), and spiced split-pea flour (Shiro) in Ethiopia.",
        "services": [
            {"title": "Premixed Shiro Powder", "icon": "bowl", "desc": "Hygienically milled split pea flour blended with ginger, garlic, red pepper, and traditional spice herbs."},
            {"title": "Berbere & Ground Spices", "icon": "pepper", "desc": "Sorted and ground red chili pepper mixed with local spices in traditional formulations."},
            {"title": "Processed Lentils & Seeds", "icon": "seed", "desc": "Cleaned and packed red lentils, flax seeds, and roasted barley flour (Beso) for retail."}
        ],
        "about": "Priem Dry Food Preparation PLC operates a dry food processing facility, sourcing raw pulses and seeds to clean, mill, and package for distribution.",
        "phone": "+251 911 876 540",
        "email": "info@priemdryfood.com",
        "form_fields": ["Distributor Name", "Dry Food Category", "Required Quantity (Quintals)"]
    },
    {
        "key": "yetna-belaynesh-metal",
        "name": "Yetna & Belaynesh General Metal Work",
        "primary": "#7c2d12", # Rusty industrial brown
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Structural Steel Fabrication & General Welding",
        "description": "Yetna & Belaynesh General Metal Work specializes in welding, custom metal doors, compound gates, and construction steel structures.",
        "services": [
            {"title": "Custom Gates & Fences", "icon": "gate", "desc": "Custom welding of sliding iron gates, compound fences, and window safety grids."},
            {"title": "Metal Door & Frames", "icon": "door", "desc": "Fabricating secure steel doors, window frames, and decorative partition grids."},
            {"title": "General Welding & Repair", "icon": "bolt", "desc": "On-site metal welding services, steel structure repair, and sheet metal fabrication."}
        ],
        "about": "Yetna & Belaynesh General Metal Work provides custom metal works and general welding services in Addis Ababa, focusing on durability and structural quality.",
        "phone": "+251 911 171 931",
        "email": "info@yetnametal.com",
        "form_fields": ["Full Name / Contractor", "Metal Fabrication Type", "Target Timeline"]
    },
    {
        "key": "tateq-metal",
        "name": "Tateq Metal Works",
        "primary": "#451a03", # Deep mahogany brown
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Precision Steel Fabrication & Metal Solutions",
        "description": "Tateq Metal Works provides professional welding, structural steel trusses, and custom steel components for construction projects.",
        "services": [
            {"title": "Steel Roof Trusses", "icon": "truss", "desc": "Design and fabrication of structural steel trusses and purlins for warehouses and industrial roofs."},
            {"title": "Industrial Structural Fitting", "icon": "crane", "desc": "Structural welding, frame alignments, and heavy steel fabrication for multi-story buildings."},
            {"title": "Ornamental Steel Work", "icon": "gate", "desc": "Custom crafting decorative steel gates, stair rails, and balcony protection grids."}
        ],
        "about": "Tateq Metal Works is a metal fabrication specialist in Ethiopia, delivering high-durability structural steel frameworks and custom welding solutions.",
        "phone": "+251 929 174 975",
        "email": "info@tateqmetal.com",
        "form_fields": ["Full Name / Contractor", "Fabrication Requirement", "Material Specification"]
    },
    {
        "key": "geedbic-consulting",
        "name": "GEEDBIC Professional Consultants",
        "primary": "#1c3d5a", # Deep slate blue
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Strategic Corporate Development & Advisory",
        "description": "GEEDBIC Professional Consultants provides management consulting, project evaluation, and capacity building services to corporate and public institutions.",
        "services": [
            {"title": "Management Advisory", "icon": "clipboard", "desc": "Assisting organizations in restructuring operations, optimizing workforce productivity, and designing corporate strategies."},
            {"title": "Project Evaluation", "icon": "chart", "desc": "Conducting comprehensive feasibility studies, financial audits, and socio-economic impact evaluations."},
            {"title": "Capacity Development", "icon": "contract", "desc": "Designing training modules and implementing corporate training programs for organizational leadership."}
        ],
        "about": "GEEDBIC Professional Consultants is an advisory firm in Ethiopia. We partner with businesses and institutions to improve performance, execute projects, and scale operations.",
        "phone": "+251 941 142 529",
        "email": "info@geedbic.com",
        "form_fields": ["Organization Name", "Consulting Area", "Project Scope"]
    },
    {
        "key": "oeiryt-consultancy",
        "name": "Oeiryt Consultancy Services",
        "primary": "#065f46", # Deep forest green
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Institutional Growth & Technical Advisory",
        "description": "Oeiryt Consultancy Services offers technical advisory, policy design, and program management services for organizations and development agencies.",
        "services": [
            {"title": "Technical Advisory", "icon": "clipboard", "desc": "Providing specialized technical consulting, system audits, and operational workflow designs."},
            {"title": "Policy & Program Design", "icon": "contract", "desc": "Assisting development agencies and institutions in policy formulation, research, and program planning."},
            {"title": "Monitoring & Evaluation", "icon": "chart", "desc": "Designing M&E frameworks, tracking program performance metrics, and delivering final evaluation reports."}
        ],
        "about": "Oeiryt Consultancy Services provides technical advisory and program management consulting to local and international institutions in East Africa.",
        "phone": "+251 901 110 086",
        "email": "info@oeiryt.com",
        "form_fields": ["Institution / Agency", "Advisory Service Required", "Expected Timeline"]
    },
    {
        "key": "yosef-legal",
        "name": "Yosef Workelule Legal Services",
        "primary": "#1c3d5a", # Deep slate blue
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Dedicated Corporate Advocacy & Legal Advisory",
        "description": "Yosef Workelule Legal Services provides legal representation, regulatory compliance guidance, and business contract advisory in Ethiopia.",
        "services": [
            {"title": "Corporate Compliance", "icon": "scales", "desc": "Guiding domestic and foreign entities through company registration, investment laws, and regulatory compliance."},
            {"title": "Contract Drafting & Review", "icon": "contract", "desc": "Drafting, reviewing, and negotiating commercial agreements, joint venture terms, and employment contracts."},
            {"title": "Dispute Resolution", "icon": "building", "desc": "Representing client interests in commercial arbitration, mediation, and civil litigation before Ethiopian courts."}
        ],
        "about": "Yosef Workelule Legal Services delivers professional legal advice and client advocacy. We specialize in corporate law, commercial agreements, and investment navigation.",
        "phone": "+251 918 505 178",
        "email": "info@yoseflegal.com",
        "form_fields": ["Client / Corporation", "Legal Matter Description", "Urgency Level"]
    },
    {
        "key": "gebru-law",
        "name": "Gebru Mahitem Law Office",
        "primary": "#1c3d5a", # Deep slate blue
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Dedicated Counsel & Professional Legal Advocacy",
        "description": "Gebru Mahitem Law Office provides commercial advisory, litigation representation, and regulatory compliance counseling in Ethiopia.",
        "services": [
            {"title": "Commercial Litigation", "icon": "scales", "desc": "Providing legal advocacy in trade disputes, property claims, tax appeals, and civil litigation before federal courts."},
            {"title": "Corporate Advisory", "icon": "contract", "desc": "Advising businesses on licensing, investment protocols, employment law, and corporate governance compliance."},
            {"title": "Contractual Services", "icon": "clipboard", "desc": "Drafting and reviewing lease agreements, supply contracts, joint venture terms, and partnership agreements."}
        ],
        "about": "Gebru Mahitem Law Office is a dedicated legal firm in Addis Ababa. We represent businesses, families, and individuals, committed to protecting their interests and delivering clear counsel.",
        "phone": "+251 940 349 840",
        "email": "info@gebrulaw.com",
        "form_fields": ["Client / Firm Name", "Practice Area", "Message Details"]
    },
    {
        "key": "hawaz-partners",
        "name": "Hawaz, Shimeles & Partners Law Office",
        "primary": "#1c3d5a", # Deep slate blue
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Comprehensive Corporate Law & Investment Advisory",
        "description": "Hawaz, Shimeles & Partners is a business law firm providing transaction advisory, intellectual property protection, and investment compliance.",
        "services": [
            {"title": "Investment Advisory", "icon": "building", "desc": "Navigating corporate clients through foreign direct investment entry, capital registration, and industrial park setups."},
            {"title": "Intellectual Property", "icon": "shield", "desc": "Registering and protecting trademarks, copyrights, patents, and industrial designs in Ethiopia and Africa."},
            {"title": "Mergers & Transactions", "icon": "contract", "desc": "Advising on equity transfers, joint ventures, asset acquisitions, and corporate finance operations."}
        ],
        "about": "Hawaz, Shimeles & Partners Law Office is a full-service commercial law firm based in Addis Ababa, serving multinational corporations and fast-growing local enterprises.",
        "phone": "+251 961 009 557",
        "email": "info@hawazlaw.com",
        "form_fields": ["Company Name", "Legal Inquiry Topic", "Message Details"]
    },
    {
        "key": "lonadd-consultancy",
        "name": "LonAdd Consultancy PLC",
        "primary": "#1c3d5a", # Deep slate blue
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Human Capital Solutions & HR Advisory",
        "description": "LonAdd Consultancy PLC is a leading human resources consulting firm in Ethiopia, providing recruitment, outsourcing, and payroll management.",
        "services": [
            {"title": "Recruitment & Executive Search", "icon": "clipboard", "desc": "Sourcing and vetting top-tier executive talent and technical specialists for multinational and local corporations."},
            {"title": "HR Outsourcing & Payroll", "icon": "contract", "desc": "Managing end-to-end payroll administration, compliance reporting, and outsourcing staffing services."},
            {"title": "Organizational Development", "icon": "chart", "desc": "Assisting client institutions with workforce structuring, performance metrics, and compliance guidelines."}
        ],
        "about": "LonAdd Consultancy PLC is a human capital advisory firm in Addis Ababa, trusted by international organizations, corporate enterprises, and NGOs to manage operations and staffing.",
        "phone": "+251 910 646 205",
        "email": "info@lonadd.com",
        "form_fields": ["Organization Name", "HR Service Requirement", "Workforce Sizing"]
    },
    {
        "key": "bridge-consulting",
        "name": "Bridge Management Consulting",
        "primary": "#065f46", # Deep forest green
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Business Strategy & Institutional Advisory",
        "description": "Bridge Management Consulting provides corporate strategy development, organizational transformation, and market intelligence advisory.",
        "services": [
            {"title": "Corporate Strategy", "icon": "chart", "desc": "Developing actionable growth strategies, market expansion plans, and operational alignment frameworks."},
            {"title": "Organizational Design", "icon": "clipboard", "desc": "Optimizing institutional setups, workflow processes, and performance accountability systems."},
            {"title": "Market Intelligence", "icon": "contract", "desc": "Delivering data-driven consumer surveys, competitor analysis, and investment feasibility audits in East Africa."}
        ],
        "about": "Bridge Management Consulting partners with corporate executives and development agencies to navigate strategy, resolve operational gaps, and accelerate performance.",
        "phone": "+251 937 997 635",
        "email": "info@bridgeconsulting.et",
        "form_fields": ["Company Name", "Advisory Scope", "Project Objectives"]
    },
    {
        "key": "kunjina-media",
        "name": "Kunjina Entertainment & Media",
        "primary": "#581c87", # Deep royal purple
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Creative Media Production & Digital Storytelling",
        "description": "Kunjina is a creative media agency specializing in video production, brand storytelling, event management, and digital content curation.",
        "services": [
            {"title": "Video Production & Adverts", "icon": "palette", "desc": "Producing high-impact television commercials, corporate documentaries, and creative social media video campaigns."},
            {"title": "Creative Brand Styling", "icon": "needle", "desc": "Designing visually striking digital campaigns, graphic assets, and social media brand templates."},
            {"title": "Event Production", "icon": "interior", "desc": "Managing corporate launch events, creative exhibitions, and promotional campaigns from concept to execution."}
        ],
        "about": "Kunjina Entertainment & Media is a digital creative boutique based in Addis Ababa, focused on delivering storytelling that engages audiences and elevates brand profiles.",
        "phone": "+251 939 063 358",
        "email": "info@kunjina.com",
        "form_fields": ["Brand / Client", "Creative Service Scope", "Target Audience"]
    },
    {
        "key": "nishan-advertising",
        "name": "Nishan Advertising & Marketing",
        "primary": "#581c87", # Deep royal purple
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Impactful Brand Solutions & Digital Marketing",
        "description": "Nishan Advertising & Marketing is a creative agency in Ethiopia delivering brand strategy, design, printing, and digital marketing setups.",
        "services": [
            {"title": "Brand Strategy & Design", "icon": "palette", "desc": "Crafting corporate visual identities, marketing collateral, logos, and promotional graphics."},
            {"title": "Digital & Social Marketing", "icon": "chart", "desc": "Executing targeted online advertising campaigns, page management, and SEO strategies."},
            {"title": "Commercial Printing & Media", "icon": "needle", "desc": "Offset and digital print production for banners, corporate brochures, and promotional merchandise."}
        ],
        "about": "Nishan Advertising & Marketing provides comprehensive branding, printing, and digital promotional services to businesses seeking to accelerate visibility in regional markets.",
        "phone": "+251 913 041 405",
        "email": "info@nishanmarketing.com",
        "form_fields": ["Organization Name", "Branding Requirement", "Campaign Budget (ETB)"],
        "active": True,
        "expiry_date": "2026-08-22"
    },
    {
        "key": "thermo-fam-trading",
        "name": "Thermo Fam Trading PLC",
        "primary": "#854d0e", # Deep bronze gold
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Industrial Equipment Sourcing & General Trading",
        "description": "Thermo Fam Trading PLC imports and distributes high-performance industrial machinery, HVAC systems, and manufacturing raw materials.",
        "services": [
            {"title": "Industrial Machinery Sourcing", "icon": "crane", "desc": "Importing and supplying heavy machinery, components, and processing equipment for local factories."},
            {"title": "HVAC & Thermal Solutions", "icon": "solar", "desc": "Providing technical supply and installation of industrial ventilation, heating, and cooling systems."},
            {"title": "Raw Materials Supply", "icon": "box", "desc": "Distributing chemical components, packaging materials, and raw inventory for local enterprises."}
        ],
        "about": "Thermo Fam Trading PLC is a trusted trading partner in Ethiopia, specializing in high-specification industrial sourcing and technical installation support.",
        "phone": "+251 953 808 080 / +251 115 530 979",
        "email": "info@thermofam.com",
        "form_fields": ["Company Name", "Equipment Specification", "Target Delivery Timeline"]
    },
    {
        "key": "golden-link-trading",
        "name": "Golden Link Trading",
        "primary": "#854d0e", # Deep bronze gold
        "font_heading": "'Playfair Display', Georgia, serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Connecting Global Logistics & Commodity Trading",
        "description": "Golden Link Trading operates general import-export activities, wholesale distribution, and commercial trade facilitation in Ethiopia.",
        "services": [
            {"title": "Agricultural Export", "icon": "grain", "desc": "Sourcing and exporting oilseeds, pulses, and specialty spices directly to regional and international ports."},
            {"title": "Consumer Goods Import", "icon": "box", "desc": "Importing and distributing raw commodities, packed food products, and household merchandise."},
            {"title": "Logistics & Facilitation", "icon": "truck", "desc": "Arranging secure customs clearance, warehousing, and corridor freight transit solutions."}
        ],
        "about": "Golden Link Trading is a diversified commercial trading partnership in Addis Ababa, connecting agricultural smallholders with global buyers and importing essential commodities.",
        "phone": "+251 930 367 784 / +251 930 367 786",
        "email": "info@goldenlinktrade.com",
        "form_fields": ["Company Name", "Commodity Category", "Inquiry Volume"]
    },
    {
        "key": "morning-star-engineering",
        "name": "Morningstar Engineering & Trading Pvt.Ltd.Co",
        "primary": "#1e3a8a", # Deep blue
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "tagline": "Precision Civil Engineering & Technical Sourcing",
        "description": "Morningstar Engineering & Trading provides civil construction engineering, structural design, and machinery distribution services.",
        "services": [
            {"title": "Civil Construction", "icon": "building", "desc": "Executing infrastructural construction, road work, building foundations, and concrete framework projects."},
            {"title": "Structural Design", "icon": "truss", "desc": "Preparing engineering drawings, structural load blueprints, and geotechnical surveys."},
            {"title": "Technical Sourcing", "icon": "crane", "desc": "Supplying certified construction machinery, heavy cranes, and concrete mixers to site developers."}
        ],
        "about": "Morningstar Engineering & Trading Pvt.Ltd.Co delivers specialized engineering contracting and commercial equipment distribution across Ethiopia.",
        "phone": "+251 911 546 405",
        "email": "info@morningstareng.com",
        "form_fields": ["Project Name / Client", "Engineering Service Scope", "Location / Region"]
    }
]

def get_google_fonts_link(c):
    fonts = set()
    fh = c["font_heading"].split("'")[1] if "'" in c["font_heading"] else "Inter"
    fb = c["font_body"].split("'")[1] if "'" in c["font_body"] else "Inter"
    fonts.add(fh.replace(" ", "+"))
    fonts.add(fb.replace(" ", "+"))
    families = "|".join([f"{f}:wght@400;600;700;800" for f in fonts])
    return f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family={families}&display=swap" rel="stylesheet">'

def get_expiry_script(c):
    expiry = c.get("expiry_date", "2026-07-16")
    active = "true" if c.get("active", True) else "false"
    return f"""
  <script>
    (function() {{
      const expiry = new Date("{expiry}");
      const active = {active};
      const now = new Date();
      if (!active || now > expiry) {{
        document.addEventListener("DOMContentLoaded", () => {{
          document.body.style.overflow = "hidden";
          document.body.style.height = "100vh";
          const lock = document.createElement("div");
          lock.style.cssText = "position:fixed; top:0; left:0; width:100vw; height:100vh; background:#faf8f5; z-index:99999; display:flex; align-items:center; justify-content:center; padding:40px; font-family:'Inter',sans-serif;";
          lock.innerHTML = `
            <div style="max-width:500px; padding:48px; background:#ffffff; border:1px solid #e7e5e4; text-align:left;">
              <div style="font-family:'Playfair Display',Georgia,serif; font-size:24px; font-weight:700; margin-bottom:16px; color:#1c1917;">Demo Period Concluded</div>
              <p style="color:#78716c; font-size:14.5px; line-height:1.6; margin-bottom:28px;">
                The review period for this custom website prototype has ended. To launch this website live, secure your custom domain, and configure corporate email servers, partner with Zemen Technologies today.
              </p>
              <a href="https://zemen.com.et/contact" target="_blank" style="display:inline-block; width:100%; text-align:center; padding:12px 24px; background:#1c3d5a; color:#ffffff; font-weight:600; font-size:13px; text-decoration:none; letter-spacing:0.05em; text-transform:uppercase; margin-bottom:24px; transition:background 0.15s;">Partner With Us</a>
              <div style="border-top:1px solid #e7e5e4; padding-top:24px;">
                <div style="font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#78716c; margin-bottom:8px;">Contact Zemen Support</div>
                <a href="tel:+251972940000" style="display:block; font-size:14px; font-weight:600; color:#1e3a8a; text-decoration:none; margin-bottom:12px;">+251 972 940 000</a>
                <a href="mailto:hello@zemen.com.et" style="display:block; font-size:14px; color:#78716c; text-decoration:none;">hello@zemen.com.et</a>
              </div>
            </div>
          `;
          document.body.appendChild(lock);
        }});
      }}
    }})();
  </script>"""

def get_custom_css(c):
    primary = c["primary"]
    font_heading = c["font_heading"]
    font_body = c["font_body"]
    bg = "#faf8f5"
    surface = "#ffffff"
    text = "#1c1917"
    muted = "#78716c"
    border = "#e7e5e4"

    return f"""
    :root {{
      --primary: {primary};
      --bg: {bg};
      --surface: {surface};
      --text: {text};
      --muted: {muted};
      --border: {border};
      --font-heading: {font_heading};
      --font-body: {font_body};
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.65; -webkit-font-smoothing: antialiased; }}
    h1, h2, h3, h4 {{ font-family: var(--font-heading); font-weight: 700; color: var(--text); }}

    /* ── LAYOUT CONTAINER ── */
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 48px;
      width: 100%;
    }}

    /* ── HEADER ── */
    header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      position: sticky; top: 0; z-index: 100;
      width: 100%;
    }}
    .header-inner {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 20px 0;
    }}
    .brand {{
      font-size: 18px; font-family: var(--font-heading); font-weight: 800;
      letter-spacing: -0.3px; text-decoration: none; color: var(--text); white-space: nowrap;
    }}
    nav {{ display: flex; align-items: center; gap: 28px; }}
    nav a {{
      text-decoration: none; color: var(--muted); font-weight: 500; font-size: 13px;
      letter-spacing: 0.02em; border-bottom: 1px solid transparent; padding-bottom: 2px;
      transition: color 0.15s, border-color 0.15s;
    }}
    nav a:hover, nav a.active {{ color: var(--primary); border-bottom-color: var(--primary); }}
    .menu-toggle {{ display: none; }}

    /* ── HERO ── */
    .hero {{
      border-bottom: 1px solid var(--border);
      background: linear-gradient(160deg, color-mix(in srgb, var(--primary) 4%, var(--bg)), var(--bg) 60%);
      width: 100%;
      padding: 96px 0 80px;
    }}
    .hero-inner {{ max-width: 720px; }}
    .hero-eyebrow {{
      display: inline-block; font-size: 11px; font-weight: 600;
      letter-spacing: 0.1em; text-transform: uppercase; color: var(--primary);
      margin-bottom: 20px;
    }}
    .hero h1 {{ font-size: 44px; line-height: 1.12; margin-bottom: 20px; }}
    .hero p {{ font-size: 16px; color: var(--muted); max-width: 540px; margin-bottom: 36px; line-height: 1.7; }}
    .btn {{
      display: inline-block; padding: 12px 28px;
      background: var(--primary); color: #fff;
      font-weight: 600; font-size: 13px; letter-spacing: 0.03em;
      border: 1px solid var(--primary); text-decoration: none;
      transition: background 0.15s, color 0.15s;
    }}
    .btn:hover {{ background: transparent; color: var(--primary); }}

    /* ── SECTIONS ── */
    .section {{ padding: 80px 0; width: 100%; }}
    .section-label {{
      font-size: 11px; font-weight: 600; letter-spacing: 0.12em;
      text-transform: uppercase; color: var(--primary); margin-bottom: 12px;
    }}
    .section-title {{ font-size: 30px; margin-bottom: 48px; }}

    /* ── SERVICE CARDS ── */
    .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); }}
    .card {{
      background: var(--surface); padding: 40px 36px;
      border: none; position: relative;
    }}
    .card-icon {{
      width: 44px; height: 44px;
      display: flex; align-items: center; justify-content: center;
      color: var(--primary); margin-bottom: 24px;
    }}
    .card h3 {{ font-size: 17px; font-weight: 700; margin-bottom: 10px; line-height: 1.3; }}
    .card p {{ color: var(--muted); font-size: 14px; line-height: 1.65; }}

    /* ── ABOUT STRIP ── */
    .about-strip {{
      background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
      padding: 64px 0;
      width: 100%;
    }}
    .about-inner {{ max-width: 760px; }}

    /* ── CONTACT ── */
    .contact-grid {{ display: grid; grid-template-columns: 1fr 1.4fr; gap: 0; background: var(--border); border: 1px solid var(--border); width: 100%; }}
    .contact-info {{ background: var(--surface); padding: 40px 36px; }}
    .contact-form {{ background: var(--surface); padding: 40px 36px; }}
    .contact-label {{ font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 6px; margin-top: 20px; }}
    .contact-label:first-child {{ margin-top: 0; }}
    .contact-value {{ font-size: 14px; font-weight: 600; color: var(--primary); text-decoration: none; display: block; line-height: 1.6; }}
    .contact-note {{ font-size: 12px; color: var(--muted); margin-top: 16px; line-height: 1.6; padding-top: 16px; border-top: 1px solid var(--border); }}
    .form-group {{ margin-bottom: 16px; }}
    .form-group label {{ display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 6px; }}
    .form-control {{
      width: 100%; padding: 10px 12px;
      border: 1px solid var(--border); background: var(--bg);
      color: var(--text); font-family: inherit; font-size: 14px; outline: none;
      transition: border-color 0.15s;
    }}
    .form-control:focus {{ border-color: var(--primary); }}

    /* ── FOOTER ── */
    footer {{ padding: 32px 0; border-top: 1px solid var(--border); background: var(--surface); width: 100%; }}
    .footer-inner {{ display: flex; justify-content: space-between; align-items: center; width: 100%; }}
    .footer-brand {{ font-family: var(--font-heading); font-weight: 800; font-size: 15px; }}
    .footer-copy {{ font-size: 12px; color: var(--muted); }}

    /* ── MOBILE ── */
    @media (max-width: 768px) {{
      .container {{ padding: 0 20px; }}
      .header-inner {{ position: relative; padding: 16px 0; }}
      .menu-toggle {{
        display: block;
        background: none;
        border: none;
        color: var(--text);
        cursor: pointer;
        padding: 4px;
        transition: color 0.15s;
      }}
      .menu-toggle:hover {{ color: var(--primary); }}
      nav {{
        display: none;
        position: absolute;
        top: 100%;
        left: -20px;
        right: -20px;
        background: var(--surface);
        border-bottom: 1px solid var(--border);
        flex-direction: column;
        padding: 24px;
        gap: 20px;
        align-items: flex-start;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        z-index: 99;
      }}
      nav.open {{ display: flex; }}
      nav a {{ width: 100%; padding: 4px 0; }}
      .hero {{ padding: 56px 0 48px; }}
      .hero h1 {{ font-size: 26px; }}
      .hero p {{ font-size: 14px; }}
      .section {{ padding: 48px 0; }}
      .grid {{ grid-template-columns: 1fr; }}
      .card {{ padding: 28px 24px; }}
      .about-strip {{ padding: 40px 0; }}
      .contact-grid {{ grid-template-columns: 1fr; }}
      .contact-info, .contact-form {{ padding: 28px 24px; }}
      footer {{ padding: 24px 0; }}
      .footer-inner {{ flex-direction: column; gap: 8px; text-align: center; }}
    }}
    """

def get_header(c, active_page):
    links = [("Home", "index.html"), ("Services", "services.html"), ("Contact", "contact.html")]
    nav_html = "".join([
        f'<a href="{url}" class="{"active" if active_page == name else ""}">{name}</a>'
        for name, url in links
    ])
    return f"""
  <header>
    <div class="container">
      <div class="header-inner">
        <a href="index.html" class="brand">{c['name']}</a>
        <button class="menu-toggle" aria-label="Toggle Menu" onclick="this.nextElementSibling.classList.toggle('open');">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
        <nav>{nav_html}</nav>
      </div>
    </div>
  </header>"""

def get_color_listener():
    return """
  <script>
    window.addEventListener('message', (e) => {{
      if (e.data && e.data.type === 'changeColor') {{
        const map = {{ blue: '#1e3a8a', purple: '#581c87', amber: '#9a3412' }};
        document.documentElement.style.setProperty('--primary', map[e.data.color] || '#854d0e');
      }}
    }});
  </script>"""

for c in companies:
    folder = os.path.join("templates", c["key"])
    os.makedirs(folder, exist_ok=True)

    if c["key"] == "hawaz-partners":
        # Custom elite styling and content for Hawaz, Shimeles & Partners Law Office
        gfonts = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
        css = """
        :root {
          --primary: #927042;
          --bg: #fdfcfb;
          --surface: #ffffff;
          --text: #11151a;
          --muted: #5c646c;
          --border: #e6e3dd;
          --font-heading: 'Cormorant Garamond', Georgia, serif;
          --font-body: 'Inter', sans-serif;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.65; -webkit-font-smoothing: antialiased; }
        h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 600; color: var(--text); }

        .container {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 48px;
          width: 100%;
        }

        header {
          background: var(--surface);
          border-bottom: 1px solid var(--border);
          position: sticky; top: 0; z-index: 100;
          width: 100%;
        }
        .header-inner {
          display: flex; justify-content: space-between; align-items: center;
          padding: 24px 0;
        }
        .brand {
          font-size: 16px; font-family: var(--font-heading); font-weight: 700;
          letter-spacing: 0.05em; text-transform: uppercase; text-decoration: none; color: var(--text); white-space: nowrap;
        }
        nav { display: flex; align-items: center; gap: 32px; }
        nav a {
          text-decoration: none; color: var(--muted); font-weight: 500; font-size: 12.5px;
          letter-spacing: 0.05em; text-transform: uppercase; border-bottom: 1px solid transparent; padding-bottom: 2px;
          transition: color 0.15s, border-color 0.15s;
        }
        nav a:hover, nav a.active { color: var(--primary); border-bottom-color: var(--primary); }
        .menu-toggle { display: none; }

        .hero {
          border-bottom: 1px solid var(--border);
          background: linear-gradient(180deg, rgba(146, 112, 66, 0.03), transparent);
          width: 100%;
          padding: 120px 0 100px;
        }
        .hero-inner { max-width: 800px; }
        .hero-eyebrow {
          display: inline-block; font-size: 11px; font-weight: 600;
          letter-spacing: 0.15em; text-transform: uppercase; color: var(--primary);
          margin-bottom: 24px;
        }
        .hero h1 { font-size: 52px; line-height: 1.1; margin-bottom: 24px; font-weight: 500; }
        .hero p { font-size: 17px; color: var(--muted); max-width: 640px; margin-bottom: 40px; line-height: 1.75; }
        .btn {
          display: inline-block; padding: 13px 32px;
          background: var(--primary); color: #fff;
          font-weight: 600; font-size: 12.5px; letter-spacing: 0.05em; text-transform: uppercase;
          border: 1px solid var(--primary); text-decoration: none;
          transition: background 0.15s, color 0.15s;
        }
        .btn:hover { background: transparent; color: var(--primary); }

        .section { padding: 96px 0; width: 100%; }
        .section-label {
          font-size: 11px; font-weight: 600; letter-spacing: 0.15em;
          text-transform: uppercase; color: var(--primary); margin-bottom: 16px;
        }
        .section-title { font-size: 36px; margin-bottom: 56px; font-weight: 500; }

        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); }
        .card {
          background: var(--surface); padding: 48px 40px;
          border: none; position: relative;
        }
        .card-icon {
          width: 44px; height: 44px;
          display: flex; align-items: center; justify-content: center;
          color: var(--primary); margin-bottom: 28px;
        }
        .card h3 { font-size: 20px; font-weight: 500; margin-bottom: 12px; line-height: 1.3; }
        .card p { color: var(--muted); font-size: 14px; line-height: 1.7; }

        .highlights-strip {
          background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
          padding: 80px 0;
          width: 100%;
        }
        .highlights-grid {
          display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px;
        }
        .highlight-item {
          text-align: center;
        }
        .highlight-value {
          font-family: var(--font-heading); font-size: 48px; font-weight: 500; color: var(--primary); margin-bottom: 8px;
        }
        .highlight-label {
          font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted);
        }

        .about-strip {
          background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
          padding: 80px 0;
          width: 100%;
        }
        .about-inner { max-width: 760px; }

        .contact-grid { display: grid; grid-template-columns: 1fr 1.4fr; gap: 0; background: var(--border); border: 1px solid var(--border); width: 100%; }
        .contact-info { background: var(--surface); padding: 48px 40px; }
        .contact-form { background: var(--surface); padding: 48px 40px; }
        .contact-label { font-size: 11px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted); margin-bottom: 8px; margin-top: 24px; }
        .contact-label:first-child { margin-top: 0; }
        .contact-value { font-size: 15px; font-weight: 600; color: var(--primary); text-decoration: none; display: block; line-height: 1.6; }
        .contact-note { font-size: 12px; color: var(--muted); margin-top: 24px; line-height: 1.6; padding-top: 24px; border-top: 1px solid var(--border); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 8px; }
        .form-control {
          width: 100%; padding: 12px;
          border: 1px solid var(--border); background: var(--bg);
          color: var(--text); font-family: inherit; font-size: 14px; outline: none;
          transition: border-color 0.15s;
          border-radius: 0px;
        }
        .form-control:focus { border-color: var(--primary); }

        footer { padding: 40px 0; border-top: 1px solid var(--border); background: var(--surface); width: 100%; }
        .footer-inner { display: flex; justify-content: space-between; align-items: center; width: 100%; }
        .footer-brand { font-family: var(--font-heading); font-weight: 700; font-size: 14px; letter-spacing: 0.05em; text-transform: uppercase; }
        .footer-copy { font-size: 12px; color: var(--muted); }
        @media (max-width: 768px) {
          .container { padding: 0 24px; }
          .header-inner { position: relative; padding: 20px 0; }
          .menu-toggle {
            display: block;
            background: none;
            border: none;
            color: var(--text);
            cursor: pointer;
            padding: 4px;
            transition: color 0.15s;
          }
          .menu-toggle:hover { color: var(--primary); }
          nav {
            display: none;
            position: absolute;
            top: 100%;
            left: -24px;
            right: -24px;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            flex-direction: column;
            padding: 24px;
            gap: 20px;
            align-items: flex-start;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
            z-index: 99;
          }
          nav.open { display: flex; }
          nav a { width: 100%; padding: 4px 0; }
          .hero { padding: 80px 0 60px; }
          .hero h1 { font-size: 32px; }
          .hero p { font-size: 15px; }
          .section { padding: 60px 0; }
          .section-title { font-size: 28px; margin-bottom: 36px; }
          .grid { grid-template-columns: 1fr; }
          .card { padding: 36px 28px; }
          .highlights-grid { grid-template-columns: 1fr; gap: 24px; }
          .highlight-value { font-size: 36px; }
          .about-strip { padding: 60px 0; }
          .contact-grid { grid-template-columns: 1fr; }
          .contact-info, .contact-form { padding: 36px 28px; }
          footer { padding: 30px 0; }
          .footer-inner { flex-direction: column; gap: 12px; text-align: center; }
        }
        """

        header_markup = f"""
      <header>
        <div class="container">
          <div class="header-inner">
            <a href="index.html" class="brand">Hawaz, Shimeles & Partners</a>
            <button class="menu-toggle" aria-label="Toggle Menu" onclick="this.nextElementSibling.classList.toggle('open');">
              <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
              </svg>
            </button>
            <nav>
              <a href="index.html" class="[active_home]">Home</a>
              <a href="services.html" class="[active_services]">Practice Areas</a>
              <a href="contact.html" class="[active_contact]">Contact</a>
            </nav>
          </div>
        </div>
      </header>"""

        # index.html
        idx_header = header_markup.replace("[active_home]", "active").replace("[active_services]", "").replace("[active_contact]", "")
        idx_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hawaz, Shimeles & Partners — Investment & Corporate Law Office</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {idx_header}
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <span class="hero-eyebrow">ADVOCATES & LEGAL ADVISORS</span>
        <h1>Guiding Enterprise Growth & Investment in East Africa</h1>
        <p>Hawaz, Shimeles & Partners is a full-service commercial law partnership based in Addis Ababa. We deliver refined legal counsel, regulatory liaison navigation, and transaction architectures for foreign investors and leading local corporations.</p>
        <a href="contact.html" class="btn">Retain Our Services</a>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <p class="section-label">Practice Areas</p>
      <h2 class="section-title">Advisory & Transactions</h2>
      <div class="grid">
        <div class="card">
          <div class="card-icon">{ICONS['building']}</div>
          <h3>FDI & Market Entry</h3>
          <p>Navigating investment gateways, obtaining commercial licenses, and structuring joint venture entities under local compliance guidelines.</p>
        </div>
        <div class="card">
          <div class="card-icon">{ICONS['shield']}</div>
          <h3>Intellectual Property</h3>
          <p>Securing, defending, and managing patent, trademark, and copyright registrations before EIPO and regional ARIPO systems.</p>
        </div>
        <div class="card">
          <div class="card-icon">{ICONS['contract']}</div>
          <h3>Transactions & M&A</h3>
          <p>Structuring equity transfers, commercial transaction agreements, and executing legal due diligence audits.</p>
        </div>
      </div>
    </div>
  </section>
  <div class="highlights-strip">
    <div class="container">
      <div class="highlights-grid">
        <div class="highlight-item">
          <div class="highlight-value">50M+ USD</div>
          <div class="highlight-label">FDI Transactions Structured</div>
        </div>
        <div class="highlight-item">
          <div class="highlight-value">200+</div>
          <div class="highlight-label">IP Assets Registered</div>
        </div>
        <div class="highlight-item">
          <div class="highlight-value">15+ Years</div>
          <div class="highlight-label">Combined Practice Expertise</div>
        </div>
      </div>
    </div>
  </div>
  <div class="about-strip">
    <div class="container">
      <div class="about-inner">
        <p class="section-label">Profile</p>
        <h2 style="font-family:var(--font-heading); font-size:24px; margin-bottom:16px; font-weight: 500;">Partnership Background</h2>
        <p style="color:var(--muted); font-size:15.5px; line-height:1.8;">Hawaz, Shimeles & Partners Law Office brings together legal practitioners with deep expertise in Ethiopian corporate law, tax structures, and regulatory liaison. We are committed to providing client advocacy that ensures security and operational compliance in regional business transactions.</p>
      </div>
    </div>
  </div>
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">Hawaz, Shimeles & Partners</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(idx_html)

        # services.html
        srv_header = header_markup.replace("[active_home]", "").replace("[active_services]", "active").replace("[active_contact]", "")
        srv_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Practice Areas — Hawaz, Shimeles & Partners</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {srv_header}
  <section class="section">
    <div class="container">
      <p class="section-label">Expertise</p>
      <h2 class="section-title">Practice Areas</h2>
      <div style="max-width:800px;">
        <div style="display:grid; grid-template-columns:56px 1fr; gap:0; align-items:start; border-bottom:1px solid var(--border); padding:36px 0;">
          <div style="color:var(--primary); padding-top:2px;">{ICONS['building']}</div>
          <div>
            <h3 style="font-size:19px; margin-bottom:10px; font-family:var(--font-heading); font-weight: 500;">FDI & Regulatory Gateways</h3>
            <p style="color:var(--muted); font-size:14.5px; line-height:1.75;">Advising international entities on market entry parameters, capital registration, and investment permit acquisition at the Ethiopian Investment Commission (EIC). We handle liaison office formations and corporate registrations from inception.</p>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:56px 1fr; gap:0; align-items:start; border-bottom:1px solid var(--border); padding:36px 0;">
          <div style="color:var(--primary); padding-top:2px;">{ICONS['shield']}</div>
          <div>
            <h3 style="font-size:19px; margin-bottom:10px; font-family:var(--font-heading); font-weight: 500;">Intellectual Property & Brand Protection</h3>
            <p style="color:var(--muted); font-size:14.5px; line-height:1.75;">Drafting IP protection frameworks, conducting trademark clearance checks, and filing registration forms before the Ethiopian Intellectual Property Office (EIPO). We represent corporate clients in regional ARIPO registration protocols and brand infringement disputes.</p>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:56px 1fr; gap:0; align-items:start; border-bottom:1px solid var(--border); padding:36px 0;">
          <div style="color:var(--primary); padding-top:2px;">{ICONS['contract']}</div>
          <div>
            <h3 style="font-size:19px; margin-bottom:10px; font-family:var(--font-heading); font-weight: 500;">Commercial Transactions & JVs</h3>
            <p style="color:var(--muted); font-size:14.5px; line-height:1.75;">Drafting and negotiating shareholder agreements, share transfer instruments, technology transfer agreements (TTA), joint venture charters, and corporate lease terms. We provide rigorous document review to secure operational priorities.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">Hawaz, Shimeles & Partners</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
        with open(os.path.join(folder, "services.html"), "w", encoding="utf-8") as f:
            f.write(srv_html)

        # contact.html
        con_header = header_markup.replace("[active_home]", "").replace("[active_services]", "").replace("[active_contact]", "active")
        con_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact & Engagement — Hawaz, Shimeles & Partners</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {con_header}
  <section class="section">
    <div class="container">
      <p class="section-label">Engagement</p>
      <h2 class="section-title">Get In Touch</h2>
      <div class="contact-grid">
        <div class="contact-info">
          <p class="contact-label">Office Telephone</p>
          <a href="tel:+251961009557" class="contact-value">+251 961 009 557</a>
          <p class="contact-label">Advisory Email</p>
          <a href="mailto:info@hawazlaw.com" class="contact-value">info@hawazlaw.com</a>
          <p class="contact-note">This secure corporate email, custom domain name, and encrypted client document locker will be registered and deployed by Zemen Technologies upon service retention agreement.</p>
        </div>
        <div class="contact-form">
          <form onsubmit="event.preventDefault(); this.style.opacity='.5'; setTimeout(()=>{{this.style.opacity='1'; this.reset();}}, 1200); alert('Advisory inquiry successfully dispatched to Hawaz, Shimeles & Partners.');">
            <div class="form-group">
              <label>Corporate Entity / Client Name</label>
              <input type="text" class="form-control" required />
            </div>
            <div class="form-group">
              <label>Practice Area of Interest</label>
              <select class="form-control" style="border-radius: 0px;" required>
                <option value="">Select a practice area...</option>
                <option value="fdi">FDI & Market Entry</option>
                <option value="ip">Intellectual Property & Trademarks</option>
                <option value="jv">Joint Ventures & Transactions</option>
                <option value="litigation">Commercial Disputes & Arbitration</option>
                <option value="other">General Advisory Consultation</option>
              </select>
            </div>
            <div class="form-group">
              <label>Estimated Transaction/Dispute Value</label>
              <select class="form-control" style="border-radius: 0px;" required>
                <option value="">Select value range...</option>
                <option value="small">Under 5 Million ETB</option>
                <option value="medium">5 Million - 25 Million ETB</option>
                <option value="large">Over 25 Million ETB / FDI Setup</option>
              </select>
            </div>
            <div class="form-group">
              <label>Matter Details & Consultation Objectives</label>
              <textarea class="form-control" rows="4" placeholder="Briefly describe the commercial objectives, regulatory hurdles, or contract terms to address..." required></textarea>
            </div>
            <button type="submit" class="btn" style="width:100%; text-align:center;">Submit Retainer Inquiry</button>
          </form>
        </div>
      </div>
    </div>
  </section>
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">Hawaz, Shimeles & Partners</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
        with open(os.path.join(folder, "contact.html"), "w", encoding="utf-8") as f:
            f.write(con_html)
        continue

    if c["key"] == "nishan-advertising":
        # Custom premium creative styling and content for Nishan Advertising & Marketing
        gfonts = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
        css = """
        :root {
          --primary: #6d28d9; /* Creative violet */
          --bg: #FAF5FF;      /* Soft lavender off-white */
          --surface: #ffffff;
          --text: #1e1b4b;     /* Deep navy charcoal */
          --muted: #6b7280;
          --border: #f3e8ff;
          --font-heading: 'Outfit', sans-serif;
          --font-body: 'Inter', sans-serif;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.65; -webkit-font-smoothing: antialiased; }
        h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 700; color: var(--text); }

        .container {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 48px;
          width: 100%;
        }

        header {
          background: var(--surface);
          border-bottom: 1px solid var(--border);
          position: sticky; top: 0; z-index: 100;
          width: 100%;
        }
        .header-inner {
          display: flex; justify-content: space-between; align-items: center;
          padding: 20px 0;
        }
        .brand {
          font-size: 20px; font-family: var(--font-heading); font-weight: 800;
          letter-spacing: -0.5px; text-decoration: none; color: var(--text); white-space: nowrap;
        }
        nav { display: flex; align-items: center; gap: 28px; }
        nav a {
          text-decoration: none; color: var(--muted); font-weight: 500; font-size: 13px;
          letter-spacing: 0.02em; border-bottom: 1px solid transparent; padding-bottom: 2px;
          transition: color 0.15s, border-color 0.15s;
        }
        nav a:hover, nav a.active { color: var(--primary); border-bottom-color: var(--primary); }
        .menu-toggle { display: none; }

        .hero {
          border-bottom: 1px solid var(--border);
          background: linear-gradient(160deg, color-mix(in srgb, var(--primary) 6%, var(--bg)), var(--bg) 60%);
          width: 100%;
          padding: 108px 0 96px;
        }
        .hero-inner { max-width: 780px; }
        .hero-eyebrow {
          display: inline-block; font-size: 11px; font-weight: 700;
          letter-spacing: 0.12em; text-transform: uppercase; color: var(--primary);
          margin-bottom: 20px;
        }
        .hero h1 { font-size: 48px; line-height: 1.1; margin-bottom: 24px; letter-spacing: -0.5px; font-weight: 800; }
        .hero p { font-size: 16.5px; color: var(--muted); max-width: 580px; margin-bottom: 36px; line-height: 1.75; }
        
        .btn {
          display: inline-block; padding: 14px 32px;
          background: var(--primary); color: #fff;
          font-weight: 600; font-size: 13px; letter-spacing: 0.05em;
          border: 1px solid var(--primary); text-decoration: none;
          text-transform: uppercase;
          transition: background 0.15s, color 0.15s;
        }
        .btn:hover { background: transparent; color: var(--primary); }

        .section { padding: 96px 0; width: 100%; }
        .section-label {
          font-size: 11px; font-weight: 700; letter-spacing: 0.12em;
          text-transform: uppercase; color: var(--primary); margin-bottom: 12px;
        }
        .section-title { font-size: 32px; margin-bottom: 56px; letter-spacing: -0.5px; font-weight: 800; }

        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; width: 100%; }
        .card {
          background: var(--surface); padding: 48px 40px;
          border: 1px solid var(--border); position: relative;
          transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
          transform: translateY(-4px);
          box-shadow: 0 12px 24px -10px color-mix(in srgb, var(--primary) 15%, transparent);
          border-color: color-mix(in srgb, var(--primary) 30%, var(--border));
        }
        .card-icon {
          width: 48px; height: 48px;
          display: flex; align-items: center; justify-content: center;
          color: var(--primary); margin-bottom: 28px;
        }
        .card h3 { font-size: 18px; font-weight: 800; margin-bottom: 12px; line-height: 1.3; }
        .card p { color: var(--muted); font-size: 14px; line-height: 1.7; }

        /* ── METRICS/HIGHLIGHTS BAR ── */
        .highlights-bar {
          background: var(--surface);
          border-top: 1px solid var(--border);
          border-bottom: 1px solid var(--border);
          padding: 56px 0;
          width: 100%;
        }
        .highlights-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 40px;
          text-align: center;
        }
        .highlight-item { display: flex; flex-direction: column; align-items: center; }
        .highlight-value {
          font-family: var(--font-heading);
          font-size: 40px;
          font-weight: 800;
          color: var(--primary);
          line-height: 1;
          margin-bottom: 8px;
        }
        .highlight-label {
          font-size: 12px;
          font-weight: 600;
          color: var(--muted);
          text-transform: uppercase;
          letter-spacing: 0.05em;
        }

        .about-strip {
          background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
          padding: 80px 0;
          width: 100%;
        }
        .about-inner { max-width: 800px; }

        .contact-grid { display: grid; grid-template-columns: 1fr 1.3fr; gap: 0; border: 1px solid var(--border); width: 100%; box-shadow: 0 8px 16px -12px rgba(0,0,0,0.1); }
        .contact-info { background: var(--surface); padding: 48px; border-right: 1px solid var(--border); }
        .contact-form { background: var(--surface); padding: 48px; }
        .contact-label { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 6px; margin-top: 24px; }
        .contact-label:first-child { margin-top: 0; }
        .contact-value { font-size: 15px; font-weight: 600; color: var(--primary); text-decoration: none; display: block; line-height: 1.6; }
        .contact-note { font-size: 12px; color: var(--muted); margin-top: 20px; line-height: 1.65; padding-top: 20px; border-top: 1px solid var(--border); }
        
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 8px; }
        .form-control {
          width: 100%; padding: 12px 14px;
          border: 1px solid var(--border); background: var(--bg);
          color: var(--text); font-family: inherit; font-size: 14px; outline: none;
          transition: border-color 0.15s, background-color 0.15s;
        }
        .form-control:focus { border-color: var(--primary); background: #ffffff; }

        footer { padding: 36px 0; border-top: 1px solid var(--border); background: var(--surface); width: 100%; }
        .footer-inner { display: flex; justify-content: space-between; align-items: center; width: 100%; }
        .footer-brand { font-family: var(--font-heading); font-weight: 800; font-size: 16px; }
        .footer-copy { font-size: 12px; color: var(--muted); }

        @media (max-width: 768px) {
          .container { padding: 0 24px; }
          .header-inner { position: relative; padding: 20px 0; }
          .menu-toggle {
            display: block;
            background: none;
            border: none;
            color: var(--text);
            cursor: pointer;
            padding: 4px;
            transition: color 0.15s;
          }
          .menu-toggle:hover { color: var(--primary); }
          nav {
            display: none;
            position: absolute;
            top: 100%;
            left: -24px;
            right: -24px;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            flex-direction: column;
            padding: 24px;
            gap: 20px;
            align-items: flex-start;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
            z-index: 99;
          }
          nav.open { display: flex; }
          nav a { width: 100%; padding: 4px 0; }
          .grid, .highlights-grid { grid-template-columns: 1fr; gap: 24px; }
          .contact-grid { grid-template-columns: 1fr; }
          .contact-info { border-right: none; border-bottom: 1px solid var(--border); }
          .hero h1 { font-size: 36px; }
        }
        """

        header_markup = f'''
        <header>
          <div class="container">
            <div class="header-inner">
              <a href="index.html" class="brand">Nishan Advertising</a>
              <button class="menu-toggle" aria-label="Toggle Menu" onclick="this.nextElementSibling.classList.toggle('open');">
                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="3" y1="12" x2="21" y2="12"></line>
                  <line x1="3" y1="6" x2="21" y2="6"></line>
                  <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
              </button>
              <nav>
                <a href="index.html" class="[active_home]">Home</a>
                <a href="services.html" class="[active_services]">Capabilities</a>
                <a href="contact.html" class="[active_contact]">Get in Touch</a>
              </nav>
            </div>
          </div>
        </header>'''

        # index.html
        idx_header = header_markup.replace("[active_home]", "active").replace("[active_services]", "").replace("[active_contact]", "")
        idx_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nishan Advertising & Marketing — Impactful Brand Solutions</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {idx_header}
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <span class="hero-eyebrow">Creative Studio & Production House</span>
        <h1>Crafting Visual Identities & Digital Stories That Drive Growth</h1>
        <p>We are a multi-disciplinary advertising and marketing agency in Addis Ababa. We partner with progressive brands to design visual campaigns, manage social growth pipelines, and deliver high-impact print media.</p>
        <a href="contact.html" class="btn">Start a Project</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <p class="section-label">Capabilities</p>
      <h2 class="section-title">Creative Services</h2>
      <div class="grid">
        <div class="card">
          <div class="card-icon">{ICONS["palette"]}</div>
          <h3>Brand Strategy & Design</h3>
          <p>We design logos, complete brand guidelines, commercial packaging, and marketing collateral that convey your corporate values and capture market attention.</p>
        </div>
        <div class="card">
          <div class="card-icon">{ICONS["chart"]}</div>
          <h3>Digital & Social Marketing</h3>
          <p>We drive consumer engagement through data-backed social media management, Telegram growth setups, targeted online ads, and localized search engine optimization.</p>
        </div>
        <div class="card">
          <div class="card-icon">{ICONS["needle"]}</div>
          <h3>Commercial Printing & Media</h3>
          <p>From offset brochures to high-fidelity large format banners, stickers, and exhibition display panels, our production workshop guarantees precision quality.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="highlights-bar">
    <div class="container">
      <div class="highlights-grid">
        <div class="highlight-item">
          <div class="highlight-value">150+</div>
          <div class="highlight-label">Brands Launched & Positioned</div>
        </div>
        <div class="highlight-item">
          <div class="highlight-value">10M+</div>
          <div class="highlight-label">Targeted Digital Ad Reach</div>
        </div>
        <div class="highlight-item">
          <div class="highlight-value">500K+</div>
          <div class="highlight-label">Quality Print Units Delivered</div>
        </div>
      </div>
    </div>
  </div>

  <div class="about-strip">
    <div class="container">
      <div class="about-inner">
        <p class="section-label">Profile</p>
        <h2 style="font-family:var(--font-heading); font-size:24px; margin-bottom:16px; font-weight: 700;">About Nishan</h2>
        <p style="color:var(--muted); font-size:15.5px; line-height:1.8;">Nishan Advertising & Marketing is a forward-thinking creative agency based in Addis Ababa, Ethiopia. We bridge the gap between creative visual artistry and strategic market positioning, helping enterprises establish authoritative brand presence across retail and digital touchpoints.</p>
      </div>
    </div>
  </div>

  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">Nishan Advertising & Marketing</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(idx_html)

        # services.html
        srv_header = header_markup.replace("[active_home]", "").replace("[active_services]", "active").replace("[active_contact]", "")
        srv_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Capabilities — Nishan Advertising & Marketing</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {srv_header}
  <section class="section">
    <div class="container">
      <p class="section-label">Capabilities</p>
      <h2 class="section-title">Our Creative & Production Suite</h2>
      <div style="max-width:800px; display:grid; gap:40px;">
        <div style="display:grid; grid-template-columns:64px 1fr; gap:0; align-items:start; border-bottom:1px solid var(--border); padding-bottom:32px;">
          <div style="color:var(--primary); padding-top:4px;">{ICONS["palette"]}</div>
          <div>
            <h3 style="font-size:20px; margin-bottom:12px; font-family:var(--font-heading); font-weight:700;">Brand Identity & Collateral Design</h3>
            <p style="color:var(--muted); font-size:15px; line-height:1.7;">Building cohesive, memorable corporate image styles from scratch. We design logos, bespoke typography packages, corporate stationery, product packaging, and print-ready files structured according to strict brand book guidelines.</p>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:64px 1fr; gap:0; align-items:start; border-bottom:1px solid var(--border); padding-bottom:32px;">
          <div style="color:var(--primary); padding-top:4px;">{ICONS["chart"]}</div>
          <div>
            <h3 style="font-size:20px; margin-bottom:12px; font-family:var(--font-heading); font-weight:700;">Digital Campaigns & Social Growth</h3>
            <p style="color:var(--muted); font-size:15px; line-height:1.7;">Managing and expanding your digital footprints. We provide creative copywriting, static and video content curation, daily channel management (Facebook, Instagram, Telegram), and hyper-targeted lead generation campaigns in Amharic and English.</p>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:64px 1fr; gap:0; align-items:start; padding-bottom:32px;">
          <div style="color:var(--primary); padding-top:4px;">{ICONS["needle"]}</div>
          <div>
            <h3 style="font-size:20px; margin-bottom:12px; font-family:var(--font-heading); font-weight:700;">Commercial Printing & Large Format Production</h3>
            <p style="color:var(--muted); font-size:15px; line-height:1.7;">Delivering high-fidelity printing services. Our production workshop processes offset publishing (company profiles, brochures, annual reports) and outdoor large-format prints (billboards, high-resolution backdrops, pull-up stands, and point-of-sale merchandise).</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">Nishan Advertising & Marketing</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
        with open(os.path.join(folder, "services.html"), "w", encoding="utf-8") as f:
            f.write(srv_html)

        # contact.html
        con_header = header_markup.replace("[active_home]", "").replace("[active_services]", "").replace("[active_contact]", "active")
        con_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Get in Touch — Nishan Advertising & Marketing</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {con_header}
  <section class="section">
    <div class="container">
      <p class="section-label">Engagement</p>
      <h2 class="section-title">Let's Build Something Together</h2>
      <div class="contact-grid">
        <div class="contact-info">
          <p class="contact-label">Creative Desk</p>
          <a href="tel:+251913041405" class="contact-value">+251 913 041 405</a>
          <p class="contact-label">Inquiry Email</p>
          <a href="mailto:info@nishanmarketing.com" class="contact-value">info@nishanmarketing.com</a>
          <p class="contact-note">This secure business email and customized website domain name will be officially registered and configured by Zemen Technologies upon signing the branding project agreement.</p>
        </div>
        <div class="contact-form">
          <form onsubmit="event.preventDefault(); this.style.opacity='.5'; setTimeout(()=>{{this.style.opacity='1'; this.reset();}}, 1200); alert('Creative proposal request successfully dispatched to Nishan Advertising.');">
            <div class="form-group">
              <label>Organization / Client Name</label>
              <input type="text" class="form-control" required />
            </div>
            <div class="form-group">
              <label>Service Scope Needed</label>
              <select class="form-control" style="border-radius: 0px;" required>
                <option value="">Select a creative service...</option>
                <option value="identity">Brand Identity & Logo Suite</option>
                <option value="digital">Social Media Growth & Marketing</option>
                <option value="printing">Commercial Printing & Collateral</option>
                <option value="production">Outdoor Billboards & Large Format</option>
                <option value="other">General Design Consulting</option>
              </select>
            </div>
            <div class="form-group">
              <label>Estimated Campaign Budget</label>
              <select class="form-control" style="border-radius: 0px;" required>
                <option value="">Select budget range...</option>
                <option value="small">Under 50,000 ETB</option>
                <option value="medium">50,000 - 250,000 ETB</option>
                <option value="large">Over 250,000 ETB</option>
              </select>
            </div>
            <div class="form-group">
              <label>Project Details & Timeline</label>
              <textarea class="form-control" rows="4" placeholder="Describe the creative challenges, marketing objectives, or print quantities required..." required></textarea>
            </div>
            <button type="submit" class="btn" style="width:100%; text-align:center;">Request Proposal</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">Nishan Advertising & Marketing</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
        with open(os.path.join(folder, "contact.html"), "w", encoding="utf-8") as f:
            f.write(con_html)
        continue

    css = get_custom_css(c)
    gfonts = get_google_fonts_link(c)

    # ── index.html ──
    header = get_header(c, "Home")
    cards_html = "".join([f"""
      <div class="card">
        <div class="card-icon">{ICONS[s['icon']]}</div>
        <h3>{s['title']}</h3>
        <p>{s['desc']}</p>
      </div>""" for s in c["services"]])

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} — {c['tagline']}</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {header}
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <span class="hero-eyebrow">Est. Addis Ababa, Ethiopia</span>
        <h1>{c['tagline']}</h1>
        <p>{c['description']}</p>
        <a href="contact.html" class="btn">Partner With Us</a>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <p class="section-label">What We Do</p>
      <h2 class="section-title">Core Services</h2>
      <div class="grid">{cards_html}</div>
    </div>
  </section>
  <div class="about-strip">
    <div class="container">
      <div class="about-inner">
        <p class="section-label">About</p>
        <h2 style="font-family:var(--font-heading); font-size:22px; margin-bottom:16px;">Our Organization</h2>
        <p style="color:var(--muted); font-size:15px; line-height:1.75;">{c['about']}</p>
      </div>
    </div>
  </div>
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">{c['name']}</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # ── services.html ──
    header = get_header(c, "Services")
    detail_html = "".join([f"""
      <div style="display:grid; grid-template-columns:56px 1fr; gap:0; align-items:start; border-bottom:1px solid var(--border); padding:36px 0;">
        <div style="color:var(--primary); padding-top:2px;">{ICONS[s['icon']]}</div>
        <div>
          <h3 style="font-size:18px; margin-bottom:10px; font-family:var(--font-heading);">{s['title']}</h3>
          <p style="color:var(--muted); font-size:14px; line-height:1.7;">{s['desc']} We provide full support, service level monitoring, and regular reviews to ensure high quality and execution standards are maintained.</p>
        </div>
      </div>""" for s in c["services"]])

    services_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Services — {c['name']}</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {header}
  <section class="section">
    <div class="container">
      <p class="section-label">Capabilities</p>
      <h2 class="section-title">Our Services</h2>
      <div style="max-width:760px;">{detail_html}</div>
    </div>
  </section>
  <div class="about-strip">
    <div class="container">
      <div class="about-inner">
        <p class="section-label">About</p>
        <h2 style="font-family:var(--font-heading); font-size:22px; margin-bottom:16px;">Our Organization</h2>
        <p style="color:var(--muted); font-size:15px; line-height:1.75;">{c['about']}</p>
      </div>
    </div>
  </div>
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">{c['name']}</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
    with open(os.path.join(folder, "services.html"), "w", encoding="utf-8") as f:
        f.write(services_html)

    # ── contact.html ──
    header = get_header(c, "Contact")
    form_inputs = "".join([f"""
        <div class="form-group">
          <label>{field}</label>
          <input type="text" class="form-control" />
        </div>""" for field in c["form_fields"]])

    phone_numbers = c["phone"].split(" / ")
    phone_html = "".join([
        f'<a href="tel:{n.replace(" ","")}" class="contact-value">{n}</a>'
        for n in phone_numbers
    ])

    contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact — {c['name']}</title>
  {FAVICON}
  {gfonts}
  <style>{css}</style>
</head>
<body>
  {header}
  <section class="section">
    <div class="container">
      <p class="section-label">Reach Us</p>
      <h2 class="section-title">Get In Touch</h2>
      <div class="contact-grid">
        <div class="contact-info">
          <p class="contact-label">Phone</p>
          {phone_html}
          <p class="contact-label">Email</p>
          <a href="mailto:{c['email']}" class="contact-value">{c['email']}</a>
          <p class="contact-note">This professional email and domain will be configured and activated by Zemen Technologies upon service agreement.</p>
        </div>
        <div class="contact-form">
          <form onsubmit="event.preventDefault(); this.style.opacity='.5'; setTimeout(()=>{{this.style.opacity='1'; this.reset();}}, 1200); alert('Inquiry dispatched to {c['name']}.');">
            {form_inputs}
            <div class="form-group">
              <label>Message</label>
              <textarea class="form-control" rows="4" placeholder="Describe your requirements and timeline..."></textarea>
            </div>
            <button type="submit" class="btn" style="width:100%; text-align:center;">Send Inquiry</button>
          </form>
        </div>
      </div>
    </div>
  </section>
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-brand">{c['name']}</span>
        <span class="footer-copy">&copy; 2026 Powered by Zemen Technologies</span>
      </div>
    </div>
  </footer>
  {get_expiry_script(c)}
  {get_color_listener()}
</body>
</html>"""
    with open(os.path.join(folder, "contact.html"), "w", encoding="utf-8") as f:
        f.write(contact_html)

print("Generated 30 pages for 10 companies with consistent max-width centering containers.")
