class Keepalive < Formula
  desc "Keep macOS awake for Teams during chosen hours"
  homepage "https://github.com/skozar/keepalive"
  version "0.2.0"
  url "https://github.com/skozar/keepalive/releases/download/v#{version}/keepalive"
  sha256 "b2e3551a83a534ea82a8be04badd2e0185aaca59d3b0fec539c94c17b572677c"

  def install
    bin.install "keepalive"
  end

  def caveats
    <<~EOS
      To start the agent:
        keepalive start

      To run with custom schedule:
        keepalive start --schedule 04:00-12:00 --idle 180

      Logs: ~/Library/Logs/keepalive/keepalive.log

      IMPORTANT: Grant Accessibility permission to keepalive:
        System Settings → Privacy & Security → Accessibility
        Add: #{opt_bin}/keepalive
    EOS
  end
end
