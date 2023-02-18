const { Client } = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200' })

client
  .search({
    index: 'social-*',
    body: {
      query: { match: { message: 'myProduct' } },
      aggs: {
        top_10_states: {
          terms: { field: 'state', size: 10 }
        }
      }
    }
  })
  .then(({ body }) => {
    const { hits } = body.hits
    console.log(hits)
  })
  .catch(console.error)