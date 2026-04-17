import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "mental-health-mcp",
    version: "1.0.0"
  },
  {
    capabilities: {
      tools: {}
    }
  }
);

// LIST TOOLS
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "mental_health_helper",
        description: "Assistente de apoio emocional",
        inputSchema: {
          type: "object",
          properties: {
            message: { type: "string" }
          },
          required: ["message"]
        }
      }
    ]
  };
});

// CALL TOOL
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "mental_health_helper") {
    const response = await fetch(
      "https://backslid-celestial-trapdoor.ngrok-free.dev/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(request.params.arguments)
      }
    );

    const data = await response.json();

    return {
      content: [
        {
          type: "text",
          text: data.response
        }
      ]
    };
  }
});

// START SERVER
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const transport = new StdioServerTransport();
await server.connect(transport);
