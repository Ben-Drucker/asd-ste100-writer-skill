#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

function parseArgs(argv) {
  const args = { target: null, force: false };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === "--target") {
      args.target = argv[i + 1] || null;
      i += 1;
      continue;
    }
    if (token === "--force") {
      args.force = true;
      continue;
    }
  }
  return args;
}

function copySkill(source, target, force) {
  if (!fs.existsSync(source)) {
    throw new Error(`Skill source path was not found: ${source}`);
  }

  const targetExists = fs.existsSync(target);
  if (targetExists && !force) {
    throw new Error(
      `Target already exists: ${target}\nUse --force to replace it.`
    );
  }

  fs.mkdirSync(path.dirname(target), { recursive: true });
  if (targetExists) {
    fs.rmSync(target, { recursive: true, force: true });
  }
  fs.cpSync(source, target, { recursive: true });
}

function run() {
  const args = parseArgs(process.argv.slice(2));
  const repoRoot = path.resolve(__dirname, "..");
  const sourceDir = path.join(repoRoot, "skills", "ste100-writer");
  const defaultTargetRoot = path.join(os.homedir(), ".claude", "skills");
  const targetRoot = args.target
    ? path.resolve(args.target)
    : defaultTargetRoot;
  const targetDir = path.join(targetRoot, "ste100-writer");

  copySkill(sourceDir, targetDir, args.force);

  process.stdout.write("Install complete.\n");
  process.stdout.write(`Skill path: ${targetDir}\n`);
}

try {
  run();
} catch (error) {
  process.stderr.write(`Install failed: ${error.message}\n`);
  process.exit(1);
}
