<!-- source: planetscale — https://planetscale.com/pricing.md -->
# PlanetScale pricing

Prices on this page based on AWS us-east-1 (N. Virginia)
Actual prices vary by cloud provider and region.

Generated at: `2026-06-26T17:47:35.386Z`

## Pricing model overview

- **Postgres**: cluster size + storage (EBS) + backups + egress + optional dedicated PgBouncer + optional additional replicas
- **Vitess**: cluster size + storage (non-metal) + optional VTGates + replicas/sharding configuration

## Postgres SKUs

### Postgres EBS HA (3-node: 1 primary + 2 replicas)

| SKU     | Architecture | vCPU | Memory  | Monthly price (USD) |
| ------- | ------------ | ---- | ------- | ------------------- |
| PS-5    | x86-64       | 1/16 | 512 MiB | $15                 |
| PS-5    | arm64        | 1/16 | 512 MiB | $15                 |
| PS-10   | arm64        | 1/8  | 1 GiB   | $30                 |
| PS-10   | x86-64       | 1/8  | 1 GiB   | $39                 |
| PS-20   | arm64        | 1/4  | 2 GiB   | $50                 |
| PS-20   | x86-64       | 1/4  | 2 GiB   | $59                 |
| PS-40   | arm64        | 1/2  | 4 GiB   | $83                 |
| PS-40   | x86-64       | 1/2  | 4 GiB   | $99                 |
| PS-80   | arm64        | 1    | 8 GiB   | $148                |
| PS-80   | x86-64       | 1    | 8 GiB   | $179                |
| PS-160  | arm64        | 2    | 16 GiB  | $286                |
| PS-160  | x86-64       | 2    | 16 GiB  | $349                |
| PS-320  | arm64        | 4    | 32 GiB  | $570                |
| PS-320  | x86-64       | 4    | 32 GiB  | $699                |
| PS-640  | arm64        | 8    | 64 GiB  | $1,135              |
| PS-640  | x86-64       | 8    | 64 GiB  | $1,399              |
| PS-1280 | arm64        | 16   | 128 GiB | $2,265              |
| PS-1280 | x86-64       | 16   | 128 GiB | $2,799              |
| PS-2560 | arm64        | 32   | 256 GiB | $4,529              |
| PS-2560 | x86-64       | 32   | 256 GiB | $5,599              |

### Postgres EBS non-HA (single node)

| SKU     | Architecture | vCPU | Memory  | Monthly price (USD) |
| ------- | ------------ | ---- | ------- | ------------------- |
| PS-5    | x86-64       | 1/16 | 512 MiB | $5                  |
| PS-5    | arm64        | 1/16 | 512 MiB | $5                  |
| PS-10   | arm64        | 1/8  | 1 GiB   | $10                 |
| PS-10   | x86-64       | 1/8  | 1 GiB   | $13                 |
| PS-20   | arm64        | 1/4  | 2 GiB   | $17                 |
| PS-20   | x86-64       | 1/4  | 2 GiB   | $20                 |
| PS-40   | arm64        | 1/2  | 4 GiB   | $28                 |
| PS-40   | x86-64       | 1/2  | 4 GiB   | $33                 |
| PS-80   | arm64        | 1    | 8 GiB   | $50                 |
| PS-80   | x86-64       | 1    | 8 GiB   | $60                 |
| PS-160  | arm64        | 2    | 16 GiB  | $96                 |
| PS-160  | x86-64       | 2    | 16 GiB  | $117                |
| PS-320  | arm64        | 4    | 32 GiB  | $190                |
| PS-320  | x86-64       | 4    | 32 GiB  | $233                |
| PS-640  | arm64        | 8    | 64 GiB  | $379                |
| PS-640  | x86-64       | 8    | 64 GiB  | $467                |
| PS-1280 | arm64        | 16   | 128 GiB | $755                |
| PS-1280 | x86-64       | 16   | 128 GiB | $933                |
| PS-2560 | arm64        | 32   | 256 GiB | $1,510              |
| PS-2560 | x86-64       | 32   | 256 GiB | $1,867              |

### Postgres metal (3-node: 1 primary + 2 replicas)

| SKU     | Architecture | vCPU | Memory   | Included storage | Monthly price (USD) |
| ------- | ------------ | ---- | -------- | ---------------- | ------------------- |
| M-10    | arm64        | 1/8  | 1 GiB    | 10 GiB           | $50                 |
| M-10    | x86-64       | 1/8  | 1 GiB    | 10 GiB           | $60                 |
| M-10    | arm64        | 1/8  | 1 GiB    | 25 GiB           | $60                 |
| M-10    | x86-64       | 1/8  | 1 GiB    | 25 GiB           | $70                 |
| M-10    | arm64        | 1/8  | 1 GiB    | 50 GiB           | $80                 |
| M-10    | x86-64       | 1/8  | 1 GiB    | 50 GiB           | $90                 |
| M-10    | arm64        | 1/8  | 1 GiB    | 100 GiB          | $110                |
| M-10    | x86-64       | 1/8  | 1 GiB    | 100 GiB          | $120                |
| M-10    | arm64        | 1/8  | 1 GiB    | 200 GiB          | $180                |
| M-10    | x86-64       | 1/8  | 1 GiB    | 200 GiB          | $200                |
| M-20    | arm64        | 1/4  | 2 GiB    | 10 GiB           | $80                 |
| M-20    | x86-64       | 1/4  | 2 GiB    | 10 GiB           | $90                 |
| M-20    | arm64        | 1/4  | 2 GiB    | 25 GiB           | $90                 |
| M-20    | x86-64       | 1/4  | 2 GiB    | 25 GiB           | $100                |
| M-20    | arm64        | 1/4  | 2 GiB    | 50 GiB           | $110                |
| M-20    | x86-64       | 1/4  | 2 GiB    | 50 GiB           | $120                |
| M-20    | arm64        | 1/4  | 2 GiB    | 100 GiB          | $140                |
| M-20    | x86-64       | 1/4  | 2 GiB    | 100 GiB          | $150                |
| M-20    | arm64        | 1/4  | 2 GiB    | 200 GiB          | $210                |
| M-20    | x86-64       | 1/4  | 2 GiB    | 200 GiB          | $230                |
| M-40    | arm64        | 1/2  | 4 GiB    | 10 GiB           | $150                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 10 GiB           | $160                |
| M-40    | arm64        | 1/2  | 4 GiB    | 25 GiB           | $160                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 25 GiB           | $170                |
| M-40    | arm64        | 1/2  | 4 GiB    | 50 GiB           | $180                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 50 GiB           | $190                |
| M-40    | arm64        | 1/2  | 4 GiB    | 100 GiB          | $200                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 100 GiB          | $210                |
| M-40    | arm64        | 1/2  | 4 GiB    | 200 GiB          | $270                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 200 GiB          | $290                |
| M-40    | arm64        | 1/2  | 4 GiB    | 400 GiB          | $330                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 400 GiB          | $340                |
| M-40    | arm64        | 1/2  | 4 GiB    | 800 GiB          | $480                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 800 GiB          | $490                |
| M-40    | arm64        | 1/2  | 4 GiB    | 1228.8 GiB       | $610                |
| M-40    | x86-64       | 1/2  | 4 GiB    | 1228.8 GiB       | $620                |
| M-80    | arm64        | 1    | 8 GiB    | 100 GiB          | $320                |
| M-80    | x86-64       | 1    | 8 GiB    | 100 GiB          | $340                |
| M-80    | arm64        | 1    | 8 GiB    | 200 GiB          | $390                |
| M-80    | x86-64       | 1    | 8 GiB    | 200 GiB          | $410                |
| M-80    | arm64        | 1    | 8 GiB    | 400 GiB          | $460                |
| M-80    | x86-64       | 1    | 8 GiB    | 400 GiB          | $480                |
| M-80    | arm64        | 1    | 8 GiB    | 800 GiB          | $600                |
| M-80    | x86-64       | 1    | 8 GiB    | 800 GiB          | $610                |
| M-80    | arm64        | 1    | 8 GiB    | 1228.8 GiB       | $740                |
| M-80    | x86-64       | 1    | 8 GiB    | 1228.8 GiB       | $750                |
| M-160   | arm64        | 2    | 16 GiB   | 100 GiB          | $570                |
| M-160   | x86-64       | 2    | 16 GiB   | 100 GiB          | $580                |
| M-160   | arm64        | 2    | 16 GiB   | 118 GiB          | $589                |
| M-160   | x86-64       | 2    | 16 GiB   | 118 GiB          | $609                |
| M-160   | arm64        | 2    | 16 GiB   | 200 GiB          | $630                |
| M-160   | x86-64       | 2    | 16 GiB   | 200 GiB          | $650                |
| M-160   | arm64        | 2    | 16 GiB   | 400 GiB          | $680                |
| M-160   | arm64        | 2    | 16 GiB   | 468 GiB          | $689                |
| M-160   | x86-64       | 2    | 16 GiB   | 400 GiB          | $720                |
| M-160   | x86-64       | 2    | 16 GiB   | 468 GiB          | $729                |
| M-160   | arm64        | 2    | 16 GiB   | 800 GiB          | $800                |
| M-160   | x86-64       | 2    | 16 GiB   | 800 GiB          | $830                |
| M-160   | arm64        | 2    | 16 GiB   | 1228.8 GiB       | $980                |
| M-160   | x86-64       | 2    | 16 GiB   | 1228.8 GiB       | $1,000              |
| M-160   | x86-64       | 2    | 16 GiB   | 1280 GiB         | $1,009              |
| M-320   | arm64        | 4    | 32 GiB   | 237 GiB          | $1,149              |
| M-320   | x86-64       | 4    | 32 GiB   | 237 GiB          | $1,179              |
| M-320   | arm64        | 4    | 32 GiB   | 937 GiB          | $1,349              |
| M-320   | x86-64       | 4    | 32 GiB   | 937 GiB          | $1,429              |
| M-320   | x86-64       | 4    | 32 GiB   | 2560 GiB         | $1,999              |
| M-640   | arm64        | 8    | 64 GiB   | 474 GiB          | $2,269              |
| M-640   | x86-64       | 8    | 64 GiB   | 474 GiB          | $2,329              |
| M-640   | arm64        | 8    | 64 GiB   | 1875 GiB         | $2,679              |
| M-640   | x86-64       | 8    | 64 GiB   | 1875 GiB         | $2,839              |
| M-640   | x86-64       | 8    | 64 GiB   | 5120 GiB         | $3,959              |
| M-960   | x86-64       | 12   | 96 GiB   | 7680 GiB         | $5,929              |
| M-1280  | arm64        | 16   | 128 GiB  | 950 GiB          | $4,499              |
| M-1280  | x86-64       | 16   | 128 GiB  | 950 GiB          | $4,629              |
| M-1280  | arm64        | 16   | 128 GiB  | 3840 GiB         | $5,319              |
| M-1280  | x86-64       | 16   | 128 GiB  | 3840 GiB         | $5,639              |
| M-1920  | x86-64       | 24   | 192 GiB  | 15360 GiB        | $11,829             |
| M-2560  | arm64        | 32   | 256 GiB  | 1945.6 GiB       | $8,979              |
| M-2560  | x86-64       | 32   | 256 GiB  | 1945.6 GiB       | $9,229              |
| M-2560  | arm64        | 32   | 256 GiB  | 7680 GiB         | $10,609             |
| M-2560  | x86-64       | 32   | 256 GiB  | 7680 GiB         | $11,249             |
| M-3840  | arm64        | 48   | 384 GiB  | 2918.4 GiB       | $13,449             |
| M-3840  | x86-64       | 48   | 384 GiB  | 2918.4 GiB       | $13,829             |
| M-3840  | arm64        | 48   | 384 GiB  | 11520 GiB        | $15,899             |
| M-3840  | x86-64       | 48   | 384 GiB  | 11520 GiB        | $16,859             |
| M-3840  | x86-64       | 48   | 384 GiB  | 30720 GiB        | $23,629             |
| M-5120  | arm64        | 64   | 512 GiB  | 3891.2 GiB       | $17,919             |
| M-5120  | x86-64       | 64   | 512 GiB  | 3891.2 GiB       | $18,439             |
| M-5120  | arm64        | 64   | 512 GiB  | 15360 GiB        | $21,189             |
| M-5120  | x86-64       | 64   | 512 GiB  | 15360 GiB        | $22,469             |
| M-5760  | x86-64       | 72   | 576 GiB  | 46080 GiB        | $35,429             |
| M-7680  | arm64        | 96   | 768 GiB  | 5836.8 GiB       | $26,869             |
| M-7680  | x86-64       | 96   | 768 GiB  | 5836.8 GiB       | $27,639             |
| M-7680  | arm64        | 96   | 768 GiB  | 23040 GiB        | $31,759             |
| M-7680  | x86-64       | 96   | 768 GiB  | 23040 GiB        | $33,689             |
| M-7680  | x86-64       | 96   | 768 GiB  | 61440 GiB        | $47,229             |
| M-10240 | x86-64       | 128  | 1024 GiB | 7782.4 GiB       | $33,509             |
| M-15360 | arm64        | 192  | 1536 GiB | 11673.6 GiB      | $48,849             |
| M-15360 | arm64        | 192  | 1536 GiB | 46080 GiB        | $63,499             |
| M-15360 | x86-64       | 192  | 1536 GiB | 46080 GiB        | $67,349             |
| M-15360 | x86-64       | 192  | 1536 GiB | 122880 GiB       | $94,429             |

## Vitess SKUs

### Vitess non-metal (3-node: 1 primary + 2 replicas)

| SKU     | Architecture | vCPU | Memory  | Monthly price (USD) |
| ------- | ------------ | ---- | ------- | ------------------- |
| PS-10   | x86-64       | 1/8  | 1 GiB   | $39                 |
| PS-20   | x86-64       | 1/4  | 2 GiB   | $59                 |
| PS-40   | x86-64       | 1/2  | 4 GiB   | $99                 |
| PS-80   | x86-64       | 1    | 8 GiB   | $179                |
| PS-160  | x86-64       | 2    | 16 GiB  | $349                |
| PS-320  | x86-64       | 4    | 32 GiB  | $699                |
| PS-400  | x86-64       | 8    | 32 GiB  | $999                |
| PS-640  | x86-64       | 8    | 64 GiB  | $1,399              |
| PS-700  | x86-64       | 16   | 32 GiB  | $1,799              |
| PS-900  | x86-64       | 16   | 64 GiB  | $1,999              |
| PS-1280 | x86-64       | 16   | 128 GiB | $2,799              |
| PS-1400 | x86-64       | 32   | 64 GiB  | $3,599              |
| PS-1800 | x86-64       | 32   | 128 GiB | $3,999              |
| PS-2560 | x86-64       | 32   | 256 GiB | $5,599              |
| PS-2100 | x86-64       | 48   | 96 GiB  | $5,399              |
| PS-2700 | x86-64       | 48   | 192 GiB | $5,999              |
| PS-2800 | x86-64       | 64   | 128 GiB | $7,199              |

### Vitess metal (3-node: 1 primary + 2 replicas)

| SKU    | Architecture | vCPU | Memory  | Included storage | Monthly price (USD) |
| ------ | ------------ | ---- | ------- | ---------------- | ------------------- |
| M-160  | x86-64       | 2    | 16 GiB  | 110 GiB          | $609                |
| M-160  | x86-64       | 2    | 16 GiB  | 460 GiB          | $758                |
| M-160  | x86-64       | 2    | 16 GiB  | 1241 GiB         | $1,009              |
| M-320  | x86-64       | 4    | 32 GiB  | 229 GiB          | $1,209              |
| M-320  | x86-64       | 4    | 32 GiB  | 929 GiB          | $1,506              |
| M-320  | x86-64       | 4    | 32 GiB  | 2490 GiB         | $2,009              |
| M-400  | x86-64       | 8    | 32 GiB  | 466 GiB          | $1,999              |
| M-640  | x86-64       | 8    | 64 GiB  | 466 GiB          | $2,419              |
| M-640  | x86-64       | 8    | 64 GiB  | 1866 GiB         | $3,002              |
| M-640  | x86-64       | 8    | 64 GiB  | 4992 GiB         | $4,019              |
| M-960  | x86-64       | 12   | 96 GiB  | 7485 GiB         | $6,179              |
| M-900  | x86-64       | 16   | 64 GiB  | 942 GiB          | $3,669              |
| M-1280 | x86-64       | 16   | 128 GiB | 942 GiB          | $4,829              |
| M-1280 | x86-64       | 16   | 128 GiB | 3739 GiB         | $6,005              |
| M-1920 | x86-64       | 24   | 192 GiB | 14992 GiB        | $12,359             |
| M-2560 | x86-64       | 32   | 256 GiB | 1891 GiB         | $9,649              |
| M-2560 | x86-64       | 32   | 256 GiB | 7492 GiB         | $11,989             |
| M-3840 | x86-64       | 48   | 384 GiB | 2842 GiB         | $15,319             |
| M-3840 | x86-64       | 48   | 384 GiB | 11242 GiB        | $18,710             |
| M-5120 | x86-64       | 64   | 512 GiB | 3792 GiB         | $19,549             |
| M-5120 | x86-64       | 64   | 512 GiB | 14992 GiB        | $23,979             |

## Region-specific requests

By default, this endpoint returns pricing for `us-east` (AWS us-east-1).

To fetch pricing for another region, add the `region` query parameter:

`https://planetscale.com/pricing.md?region=<region_identifier>`

Example:

`https://planetscale.com/pricing.md?region=eu-west`

The `region` value must match one of the supported identifiers below.

| Region identifier           | Region                      |
| --------------------------- | --------------------------- |
| ap-northeast                | AWS ap-northeast-1          |
| ap-south                    | AWS ap-south-1              |
| ap-southeast                | AWS ap-southeast-1          |
| aws-ap-southeast-2          | AWS ap-southeast-2          |
| aws-ca-central-1            | AWS ca-central-1            |
| eu-central                  | AWS eu-central-1            |
| eu-west                     | AWS eu-west-1               |
| aws-eu-west-2               | AWS eu-west-2               |
| aws-sa-east-1               | AWS sa-east-1               |
| us-east                     | AWS us-east-1               |
| aws-us-east-2               | AWS us-east-2               |
| us-west                     | AWS us-west-2               |
| gcp-asia-northeast3         | GCP asia-northeast3         |
| gcp-europe-west1            | GCP europe-west1            |
| gcp-europe-west4            | GCP europe-west4            |
| gcp-northamerica-northeast1 | GCP northamerica-northeast1 |
| gcp-us-central1             | GCP us-central1             |
| gcp-us-east1                | GCP us-east1                |
| gcp-us-east4                | GCP us-east4                |
