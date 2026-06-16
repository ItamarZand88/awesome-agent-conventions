<!-- source: HimangshuPronoy-fame2 — https://raw.githubusercontent.com/HimangshuPronoy/fame2/main/.kiro/steering/tech.md -->
# Tech Stack

## Framework & Runtime
- **Next.js 15.1.11** (App Router)
- **React 19** with TypeScript
- **Node.js** runtime

## Backend & Database
- **Supabase** for authentication and PostgreSQL database
- Row Level Security (RLS) policies for data access control
- Two client modes:
  - `supabase`: Public client (respects RLS) - use in client components and most server code
  - `supabaseAdmin`: Admin client (bypasses RLS) - ONLY use in Server Actions/API routes

## Styling
- **CSS Modules** for component styling (`.module.css` files)
- Component-scoped styles with camelCase class names
- Global styles in `src/app/globals.css`

## Key Libraries
- `@supabase/supabase-js`: Database and auth client
- `framer-motion`: Animations
- `lucide-react`: Icon library
- `next/image`: Optimized image loading (configured for Unsplash)

## Common Commands
```bash
npm run dev      # Start development server (http://localhost:3000)
npm run build    # Production build
npm run start    # Start production server
npm run lint     # Run ESLint
```

## Environment Variables
Required in `.env.local`:
- `NEXT_PUBLIC_SUPABASE_URL`: Supabase project URL
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`: Supabase anonymous key
- `SUPABASE_SERVICE_ROLE_KEY`: Service role key (for admin operations)

## TypeScript Configuration
- Strict mode enabled
- Path alias: `@/*` maps to `./src/*`
- Target: ES2017
