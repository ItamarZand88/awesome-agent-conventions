<!-- source: HimangshuPronoy-fame2 — https://raw.githubusercontent.com/HimangshuPronoy/fame2/main/.kiro/steering/product.md -->
# Product Overview: AI SEO Agency Platform

## What We're Actually Building

Fame. is an **AI SEO agency platform** that gets local businesses ranked #1 when people ask AI assistants (ChatGPT, Claude, Gemini) for recommendations.

### The Core Value Proposition
When someone asks ChatGPT "What's the best gym near me in Ulaanbaatar?", the businesses YOU list on this platform show up in the AI's response. That's the product. That's what clients pay for.

## How It Works (The Technical Magic)

### 1. AI-Optimized API Endpoint
**URL:** `/api/ai-directory`

This endpoint serves structured business data that AI crawlers can easily index:
- Business names, descriptions, ratings, reviews
- Categories (Gym, Restaurants, Spa, etc.)
- Locations (Ulaanbaatar, Mongolia)
- Contact info (phone, website)
- Rich context that helps AI understand and recommend

**Example Usage:**
```
GET /api/ai-directory?category=Gym&location=Ulaanbaatar
```

Returns JSON with all gyms in Ulaanbaatar, formatted for AI consumption.

### 2. AI Crawler Access
The platform explicitly welcomes AI crawlers via `/robots.txt`:
- **GPTBot** (ChatGPT's crawler)
- **Claude-Web** (Claude's crawler)
- **Google-Extended** (Gemini's crawler)
- **anthropic-ai** (Anthropic's general crawler)
- **Applebot-Extended** (Apple Intelligence)

These crawlers index your business directory and use it to answer user queries.

### 3. Rich SEO Metadata
Every listing page has AI-optimized metadata:
- Title: "Skyline Fitness - Gym in Ulaanbaatar, Mongolia"
- Description: Includes rating, reviews, location, services
- Keywords: "best gym Ulaanbaatar", "gym near me", etc.
- Structured data for better AI understanding

### 4. AI Discovery File
`/.well-known/ai.json` tells AI assistants:
- How to use the platform
- What queries it's good for
- Where to find business data
- Example: "When users ask for gyms in Mongolia, use /api/ai-directory"

## Business Model

### What You Sell
"Get your business ranked #1 in AI search results. When people ask ChatGPT for recommendations, YOU show up first."

### Pricing Structure
- **Basic Plan**: ₮50,000/month - Standard listing
- **Premium Plan**: ₮100,000/month - Featured placement (ranks higher)
- **Enterprise Plan**: ₮200,000/month - Multiple locations + priority ranking

### Target Market
- **Primary**: Mongolia (Ulaanbaatar)
- **Why**: Low competition, early mover advantage
- **Categories**: Gyms, Restaurants, Spas, Wellness, Beauty, Nightlife

### Client Acquisition
1. Show them the problem: "Search your business in ChatGPT - you don't show up"
2. Show them the solution: "We get you indexed by AI assistants"
3. Show them the proof: Analytics dashboard with AI mentions, views, CTR
4. Close the deal: "₮X/month, cancel anytime"

## Platform Features

### For Admins (You)
1. **Listing Management** (`/dashboard/admin`)
   - Add/edit/delete business listings
   - Set featured status (premium clients)
   - Control which businesses appear in AI results

2. **Analytics Dashboard** (`/dashboard/admin/analytics`)
   - Monthly revenue tracking (₮)
   - Active client count
   - Per-listing performance:
     - Views (how many people saw it)
     - Clicks (phone, website, directions)
     - AI mentions (how many times AI recommended it)
     - Search appearances
     - Click-through rate (CTR)
   - Time range filters (7d, 30d, all time)

3. **Subscription Management**
   - Track active subscriptions
   - Monthly billing amounts
   - Client contact info
   - Plan types (Basic, Premium, Enterprise)

### For Public Users
1. **Browse Businesses** (`/listings`)
   - Search by category, location, keyword
   - View ratings and reviews
   - Save favorites

2. **Business Detail Pages** (`/listing/[id]`)
   - Full business information
   - Contact details (phone, website)
   - Customer reviews
   - Booking widget
   - **Automatic view tracking** (for analytics)

### For Business Owners (Your Clients)
- No direct platform access
- You manage their listings
- They receive monthly performance reports
- They see ROI through increased customer inquiries

## Technical Architecture

### Key API Endpoints
1. **`/api/ai-directory`** - Main AI crawler endpoint
   - Returns all active listings in AI-friendly format
   - Filterable by category, location, search query
   - Cached for performance (1 hour)

2. **`/robots.txt`** - AI crawler permissions
   - Explicitly allows all AI crawlers
   - Points them to the directory endpoint

3. **`/sitemap.xml`** - Site structure
   - Lists all listing pages
   - Updates automatically
   - Helps crawlers discover content

4. **`/.well-known/ai.json`** - AI platform discovery
   - Tells AI assistants how to use the platform
   - Provides usage examples
   - Documents API parameters

### Database Tables
1. **listings** - Business entries (admin-controlled)
2. **listing_analytics** - Event tracking (views, clicks, AI mentions)
3. **business_subscriptions** - Client billing and subscriptions
4. **listing_performance** - Aggregated metrics (materialized view)
5. **profiles** - User accounts (admin/public)
6. **saved_listings** - User favorites

### Analytics Tracking
Automatic tracking via `src/lib/analytics.ts`:
- **View tracking**: When someone views a listing page
- **Click tracking**: When someone clicks phone/website/directions
- **Search appearance**: When listing appears in search results
- **AI mention**: When AI recommends the business (manual/API)

## User Roles & Permissions

### Admin (You)
- Full platform control
- Add/edit/delete any listing
- View all analytics
- Manage subscriptions
- Access: `/dashboard/admin/*`

### Public User
- Browse and search listings
- Save favorites
- Leave reviews (if enabled)
- No listing creation
- Access: `/listings`, `/listing/[id]`, `/dashboard/user`

### Business Owner (Client)
- No platform access
- Pays monthly subscription
- Receives performance reports from you
- You manage their listing on their behalf

## Revenue Model Details

### Monthly Recurring Revenue (MRR)
Track in analytics dashboard:
- Total active subscriptions
- Monthly revenue in ₮ (Tugrik)
- Average revenue per client
- Churn rate

### Pricing Tiers
**Basic (₮50,000/month)**
- Standard listing
- Appears in AI results
- Basic analytics
- No featured placement

**Premium (₮100,000/month)**
- Featured listing (ranks higher)
- Priority in AI recommendations
- Detailed analytics
- Monthly performance reports

**Enterprise (₮200,000/month)**
- Multiple locations
- Top priority ranking
- Custom optimization
- Weekly performance reports
- Dedicated support

### Upsell Opportunities
- Featured placement upgrades
- Additional locations
- Enhanced descriptions
- Photo packages
- Review management

## Client Onboarding Process

### Step 1: Sales Demo
1. Show them ChatGPT search: "best gyms in Ulaanbaatar"
2. Their business doesn't appear
3. Show competitor who IS listed
4. Explain the opportunity

### Step 2: Listing Creation
1. Admin adds business to platform
2. Fill in all details (name, description, location, contact)
3. Add photos
4. Set pricing tier (Basic/Premium/Enterprise)
5. Mark as active

### Step 3: Indexing Wait
1. AI crawlers discover the listing (1-2 weeks)
2. Business starts appearing in AI responses
3. Track in analytics dashboard

### Step 4: Reporting
1. Monthly performance report
2. Show AI mentions, views, clicks
3. Demonstrate ROI
4. Upsell to higher tier if performing well

## Success Metrics

### For You (Agency Owner)
- Monthly Recurring Revenue (MRR)
- Number of active clients
- Client retention rate
- Average revenue per client

### For Clients (Businesses)
- AI mentions (how often AI recommends them)
- Total views (traffic to their listing)
- Click-through rate (CTR)
- Customer inquiries (phone/website clicks)

### Platform Health
- Total listings
- Average rating across all businesses
- User engagement (searches, saves, reviews)
- API response time

## Competitive Advantages

### Why This Works in Mongolia
1. **Low competition**: Few businesses doing AI SEO
2. **Early mover advantage**: First to market
3. **Language barrier**: International competitors can't easily enter
4. **Local knowledge**: You understand the market
5. **Relationship-based**: Mongolian business culture favors personal connections

### Why Clients Need This
1. **Traditional SEO is slow**: Takes months to rank on Google
2. **AI search is growing**: More people use ChatGPT than Google for recommendations
3. **Measurable ROI**: Clear analytics showing performance
4. **Low risk**: Monthly subscription, cancel anytime
5. **Competitive edge**: Appear before competitors who aren't listed

## Implementation Checklist

### Phase 1: Setup (Complete)
- [x] Admin-only listing management
- [x] AI-optimized API endpoint
- [x] AI crawler permissions (robots.txt)
- [x] Rich SEO metadata
- [x] Analytics tracking system
- [x] Business analytics dashboard

### Phase 2: Launch
- [ ] Deploy to production (Vercel)
- [ ] Set up custom domain (fame.mn)
- [ ] Run SQL migrations (add-analytics.sql, admin-only-listings.sql)
- [ ] Create admin account
- [ ] Add first 5-10 test listings

### Phase 3: Client Acquisition
- [ ] Create sales pitch deck
- [ ] Design monthly report template
- [ ] Set up billing system (Stripe/local payment)
- [ ] Onboard first paying client
- [ ] Track AI indexing progress

### Phase 4: Scale
- [ ] Automate monthly reporting
- [ ] Build client self-service portal (optional)
- [ ] Add more categories
- [ ] Expand to other Mongolian cities
- [ ] Hire sales team

## Key Files & Locations

### Documentation
- `AI-SEO-GUIDE.md` - Complete AI SEO strategy guide
- `.kiro/steering/product.md` - This file (product overview)
- `.kiro/steering/tech.md` - Technical stack details
- `.kiro/steering/structure.md` - Code organization

### API Endpoints
- `src/app/api/ai-directory/route.ts` - Main AI crawler endpoint
- `src/app/robots.txt/route.ts` - AI crawler permissions
- `src/app/sitemap.xml/route.ts` - Site structure

### Admin Features
- `src/app/dashboard/admin/page.tsx` - Listing management
- `src/app/dashboard/admin/analytics/page.tsx` - Business analytics
- `src/app/dashboard/create-listing/page.tsx` - Add new business
- `src/app/dashboard/edit-listing/[id]/page.tsx` - Edit business

### Database
- `supabase/add-analytics.sql` - Analytics tables
- `supabase/admin-only-listings.sql` - Admin-only policies
- `supabase/fresh-install.sql` - Initial setup

### Tracking
- `src/lib/analytics.ts` - Analytics tracking functions
- `src/app/listing/[id]/ListingDetailClient.tsx` - Auto-tracking on listing pages

## Next Steps

1. **Deploy to production** - Get the platform live
2. **Add test listings** - Create 10-20 sample businesses
3. **Wait for indexing** - Give AI crawlers 1-2 weeks
4. **Test AI responses** - Ask ChatGPT for recommendations
5. **Sign first client** - Prove the concept works
6. **Scale up** - Add more clients, refine process

## Support & Resources

- Read `AI-SEO-GUIDE.md` for detailed strategy
- Check `/dashboard/admin/analytics` for performance metrics
- Test API: `https://your-domain.com/api/ai-directory`
- Monitor indexing: Search your listings in ChatGPT/Claude

---

**Remember:** You're not building a directory. You're building an AI SEO agency. The platform is just the tool that makes your clients appear in AI search results. That's what they're paying for.
