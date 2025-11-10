# Trigger GitHub Issue Creation via Webhook

## Setup

The repository now has a `repository_dispatch` workflow that can be triggered externally.

## How to Trigger

### Using curl (for testing):

```bash
curl -X POST \
  https://api.github.com/repos/qyntec/qyntec.ai/dispatches \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -d '{
    "event_type": "form_submission",
    "client_payload": {
      "email": "test@example.com",
      "timestamp": "2024-11-10T15:00:00Z",
      "source": "Landing Page"
    }
  }'
```

### From Google Apps Script:

```javascript
function triggerGitHubIssue(email) {
  const url = 'https://api.github.com/repos/qyntec/qyntec.ai/dispatches';
  const token = 'YOUR_GITHUB_TOKEN'; // Store in Script Properties
  
  const payload = {
    event_type: 'form_submission',
    client_payload: {
      email: email,
      timestamp: new Date().toISOString(),
      source: 'Google Form'
    }
  };
  
  const options = {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json'
    },
    payload: JSON.stringify(payload)
  };
  
  UrlFetchApp.fetch(url, options);
}
```

### From Zapier/Make.com:

1. **Trigger:** Form submission (Formspree, Google Forms, etc.)
2. **Action:** Webhooks by Zapier
   - Method: POST
   - URL: `https://api.github.com/repos/qyntec/qyntec.ai/dispatches`
   - Headers:
     - `Authorization`: `Bearer YOUR_GITHUB_TOKEN`
     - `Accept`: `application/vnd.github.v3+json`
   - Body:
     ```json
     {
       "event_type": "form_submission",
       "client_payload": {
         "email": "{{email}}",
         "timestamp": "{{timestamp}}",
         "source": "Formspree"
       }
     }
     ```

## Creating a GitHub Token

1. Go to https://github.com/settings/tokens?type=beta
2. Click "Generate new token"
3. Select repository: `qyntec/qyntec.ai`
4. Permissions needed:
   - **Contents:** Read-only
   - **Metadata:** Read-only
   - **Issues:** Read and write
5. Generate and copy the token
6. Store securely (never commit to git!)

## Testing

After triggering, check:
- Actions tab: https://github.com/qyntec/qyntec.ai/actions
- Issues tab: https://github.com/qyntec/qyntec.ai/issues

## Security Note

The GitHub token should be stored securely:
- In Google Apps Script: Use Script Properties
- In Zapier: Use Zapier's secure storage
- Never expose in client-side code
