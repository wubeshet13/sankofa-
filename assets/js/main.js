// Template Data Map
const templates = {
  coffee: {
    name: 'Abyssinia Specialty Coffee',
    desc: 'Modern Cafe & Coffee Roasters website',
    url: 'templates/coffee-shop/index.html'
  },
  clinic: {
    name: 'Zemen Clinic & Diagnostic',
    desc: 'Medical practice & clinic scheduling site',
    url: 'templates/clinic/index.html'
  },
  school: {
    name: 'Zemen Academy & Kindergarten',
    desc: 'Interactive school curriculum & parent portal',
    url: 'templates/school/index.html'
  },
  priemdryfood: {
    name: 'Priem Dry Food',
    desc: 'Hygienic spices & processed pulses catalog',
    url: 'templates/priem-dry-food/index.html'
  },
  techstartup: {
    name: 'Zemen SaaS Portal',
    desc: 'Futuristic startup landing page',
    url: 'templates/tech-startup/index.html'
  },
  fintech: {
    name: 'Zemen Pay',
    desc: 'Sleek mobile finance & wallet landing page',
    url: 'templates/fintech/index.html'
  },
  ecommerce: {
    name: 'Zemen Luxury Store',
    desc: 'High-end traditional fashion e-shop',
    url: 'templates/e-commerce/index.html'
  },
  akidtrading: {
    name: 'Akid Trading PLC',
    desc: 'Import/Export & General Trading catalog',
    url: 'templates/akid-trading/index.html'
  },
  nuriyemetal: {
    name: 'Nuriye Netsanet Metal Works',
    desc: 'Heavy structural steel & fabrication services',
    url: 'templates/nuriye-netsanet-metal/index.html'
  },
  metigarment: {
    name: 'Meti Mekonnen Garment',
    desc: 'Apparel manufacturing & wholesale uniforms',
    url: 'templates/meti-mekonnen-garment/index.html'
  },
  danieltransport: {
    name: 'Daniel Freight Transport',
    desc: 'Cross-border logistics & dry cargo transport',
    url: 'templates/daniel-tesfaye-freight/index.html'
  },
  etegedesign: {
    name: 'Etege Design',
    desc: 'Premium fashion heritage & creative branding',
    url: 'templates/etege-design/index.html'
  },
  brightafrica: {
    name: 'Bright Africa',
    desc: 'Tech solutions & solar renewable energy systems',
    url: 'templates/bright-africa/index.html'
  },
  checkpointsecurity: {
    name: 'Check Point Security & Clean',
    desc: 'Facilities management, guard & janitorial service',
    url: 'templates/checkpoint-security/index.html'
  },
  eyuelstationery: {
    name: 'Eyuel & Yonathan Trade',
    desc: 'Wholesale stationery & computer accessories',
    url: 'templates/eyuel-yonathan-stationery/index.html'
  },
  desalegnmetal: {
    name: 'Desalegn Metal Work',
    desc: 'Ornamental residential steel gates & handrails',
    url: 'templates/desalegn-metal/index.html'
  },
  yetnabelayneshmetal: {
    name: 'Yetna & Belaynesh General Metal Work',
    desc: 'Custom gates, steel doors, and general welding',
    url: 'templates/yetna-belaynesh-metal/index.html'
  },
  tateqmetal: {
    name: 'Tateq Metal Works',
    desc: 'Precision structural steel trusses & metal works',
    url: 'templates/tateq-metal/index.html'
  },
  geedbicconsulting: {
    name: 'GEEDBIC Professional Consultants',
    desc: 'Management advisory & capacity development systems',
    url: 'templates/geedbic-consulting/index.html'
  },
  oeirytconsultancy: {
    name: 'Oeiryt Consultancy Services',
    desc: 'Institutional policy, technical advisory & program design',
    url: 'templates/oeiryt-consultancy/index.html'
  },
  yoseflegal: {
    name: 'Yosef Workelule Legal Services',
    desc: 'Dedicated corporate law, contracts & dispute advocacy',
    url: 'templates/yosef-legal/index.html'
  },
  gebrulaw: {
    name: 'Gebru Mahitem Law Office',
    desc: 'Professional litigation, commercial advisory & compliance',
    url: 'templates/gebru-law/index.html'
  },
  hawazpartners: {
    name: 'Hawaz, Shimeles & Partners Law Office',
    desc: 'Corporate transactions, investment advisory & trademark systems',
    url: 'templates/hawaz-partners/index.html'
  },
  lonaddconsultancy: {
    name: 'LonAdd Consultancy PLC',
    desc: 'Human resources consulting, recruitment & payroll systems',
    url: 'templates/lonadd-consultancy/index.html'
  },
  bridgeconsulting: {
    name: 'Bridge Management Consulting',
    desc: 'Business growth strategy & institutional advisory',
    url: 'templates/bridge-consulting/index.html'
  },
  kunjinamedia: {
    name: 'Kunjina Entertainment & Media',
    desc: 'Creative video production, branding & digital storytelling',
    url: 'templates/kunjina-media/index.html'
  },
  nishanadvertising: {
    name: 'Nishan Advertising & Marketing',
    desc: 'Visual branding, digital marketing & print advertising',
    url: 'templates/nishan-advertising/index.html'
  },
  thermofamtrading: {
    name: 'Thermo Fam Trading PLC',
    desc: 'Industrial machinery, HVAC systems & general import-export',
    url: 'templates/thermo-fam-trading/index.html'
  },
  goldenlinktrading: {
    name: 'Golden Link Trading',
    desc: 'Agricultural commodity export, logistics & cargo distribution',
    url: 'templates/golden-link-trading/index.html'
  },
  morningstarengineering: {
    name: 'Morningstar Engineering & Trading',
    desc: 'Civil engineering designs, structural blueprints & machine supply',
    url: 'templates/morning-star-engineering/index.html'
  }
};

// Packages Content Map
const packages = {
  starter: {
    title: 'Starter Package',
    subtitle: 'For Small Businesses & Startups',
    features: [
      'Company Website (modern, mobile-first, multilingual if needed)',
      'Custom Domain & Hosting Setup (e.g. yourname.zai.et or .com)',
      'Business Emails (yourname@company.et)',
      'Logo & Brand Identity Kit (colors, typography, guidelines)',
      'Digital Business Cards (print + NFC-enabled options)',
      'Basic Social Media Setup (Facebook, Instagram, LinkedIn)',
      'Google Maps & Google Business Profile Setup',
      'Introductory IT Consultation'
    ],
    cta: 'Get Started with Starter'
  },
  growth: {
    title: 'Growth Package',
    subtitle: 'For SMEs Expanding Operations',
    features: [
      'Everything in Starter Package, plus:',
      'E-Commerce Website (catalog, cart, Telebirr/CBE payments integration)',
      'Company Profile Design (brochures, flyers, pitch decks)',
      'Business Management Software (POS, Inventory, HR tools)',
      'SEO Optimization & Online Ads Management',
      'Social Media Marketing (content strategy, posting campaigns)',
      'Basic Data Dashboards (sales, expenses, KPIs)',
      'Cybersecurity Starter Tools (SSL, backups, malware protection)'
    ],
    cta: 'Scale Up with Growth'
  },
  enterprise: {
    title: 'Enterprise Package',
    subtitle: 'For Large Corporations',
    features: [
      'Everything in Growth Package, plus:',
      'Full ERP System Development (HR, Finance, Sales, Inventory, Supply Chain, Payroll)',
      'Custom CRM Platform (customer management, leads tracking, follow-ups)',
      'Mobile Applications (iOS & Android – for business services/products)',
      'Cloud Hosting & Automated Data Backup (AWS, Azure, Google Cloud)',
      'Advanced Cybersecurity & Data Compliance (penetration testing, ISO standards)',
      'AI-Powered Analytics Dashboards (predictive insights, forecasting)',
      'API Integrations (banks, logistics, custom APIs)',
      '24/7 IT Support & Maintenance'
    ],
    cta: 'Transform with Enterprise'
  },
  digital: {
    title: 'Digital Transformation',
    subtitle: 'For Institutions & NGOs',
    features: [
      'Tailored solutions for schools, NGOs, and government bodies:',
      'Learning Management Systems (LMS) & Virtual Classrooms',
      'Student/Staff Portals & custom e-Services',
      'Custom Research & Survey Platforms',
      'Document Digitization & secure e-Archives',
      'Donor & Beneficiary Management Systems',
      'Localization & Multilingual Systems (Amharic, Afan Oromo, Tigrinya, etc.)'
    ],
    cta: 'Deploy Digital Transformation'
  }
};

let currentTemplate = 'coffee';

document.addEventListener('DOMContentLoaded', () => {
  const iframe = document.getElementById('preview-iframe');
  
  // Theme Switcher Logic
  const themeToggle = document.getElementById('theme-toggle');
  themeToggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('light-theme');
  });

  // Template Switcher Logic
  const templateButtons = document.querySelectorAll('.template-item');
  templateButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active class from all
      templateButtons.forEach(b => b.classList.remove('active'));
      // Add active class to clicked
      btn.classList.add('active');
      
      const key = btn.dataset.template;
      currentTemplate = key;
      
      // Update preview header details
      document.getElementById('active-template-name').textContent = templates[key].name;
      
      // Update iframe source
      iframe.src = templates[key].url;
    });
  });

  // Deep-link template router via URL Hash (e.g. demo.zai.et#akidtrading)
  function handleHashRoute() {
    const hash = window.location.hash.replace('#', '');
    if (hash && templates[hash]) {
      currentTemplate = hash;
      templateButtons.forEach(b => {
        if (b.dataset.template === hash) {
          b.classList.add('active');
          // Scroll button into view in the sidebar
          b.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          b.classList.remove('active');
        }
      });
      document.getElementById('active-template-name').textContent = templates[hash].name;
      iframe.src = templates[hash].url;
    }
  }

  // Handle hash on initial load
  window.addEventListener('load', handleHashRoute);
  // Handle hash changes dynamically
  window.addEventListener('hashchange', handleHashRoute);

  // Responsive Controls Sizing Logic
  const controlButtons = document.querySelectorAll('.control-btn');
  controlButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      controlButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      const device = btn.dataset.device;
      if (device === 'desktop') {
        iframe.style.width = '100%';
      } else if (device === 'tablet') {
        iframe.style.width = '768px';
      } else if (device === 'mobile') {
        iframe.style.width = '375px';
      }
    });
  });

  // Color Palette Customizer (Sends color changes to the template inside iframe via postMessage)
  const colorDots = document.querySelectorAll('.color-dot');
  colorDots.forEach(dot => {
    dot.addEventListener('click', () => {
      colorDots.forEach(d => d.classList.remove('active'));
      dot.classList.add('active');
      
      const color = dot.dataset.color;
      
      // Send color command to the iframe
      iframe.contentWindow.postMessage({ type: 'changeColor', color: color }, '*');
    });
  });

  // Keep color choice in sync on template load
  iframe.addEventListener('load', () => {
    const activeDot = document.querySelector('.color-dot.active');
    if (activeDot) {
      const color = activeDot.dataset.color;
      iframe.contentWindow.postMessage({ type: 'changeColor', color: color }, '*');
    }
  });

  // Modal Package Details Dialog Logic
  const packagePills = document.querySelectorAll('.package-pill');
  const modalOverlay = document.getElementById('modal-overlay');
  const modalClose = document.getElementById('modal-close');
  
  packagePills.forEach(pill => {
    pill.addEventListener('click', () => {
      const key = pill.dataset.package;
      const data = packages[key];
      
      document.getElementById('modal-subtitle').textContent = data.title;
      document.getElementById('modal-title').textContent = data.subtitle;
      
      const list = document.getElementById('modal-features');
      list.innerHTML = '';
      data.features.forEach(feat => {
        const li = document.createElement('li');
        li.innerHTML = `<i data-lucide="check-circle-2"></i> <span>${feat}</span>`;
        list.appendChild(li);
      });
      
      // Set Inquiry button href
      const inquireBtn = document.getElementById('modal-inquire-btn');
      inquireBtn.textContent = data.cta;
      inquireBtn.href = `https://t.me/zemen_tech_bot?start=inquire_${key}`;
      
      // Open modal
      modalOverlay.style.display = 'flex';
      lucide.createIcons();
    });
  });

  modalClose.addEventListener('click', () => {
    modalOverlay.style.display = 'none';
  });

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
      modalOverlay.style.display = 'none';
    }
  });
});
